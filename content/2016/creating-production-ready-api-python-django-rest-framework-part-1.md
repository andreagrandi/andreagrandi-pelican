Title: Creating a production ready API with Python and Django Rest Framework - part 1
Date: 2016-09-28 13:47
Author: Andrea Grandi
Category: Development
Tags: API, Django, framework, Python, rest, tutorial
Slug: creating-production-ready-api-python-django-rest-framework-part-1
Status: published

The aim if this tutorial is to show how to create a production ready
solution for a **REST API**, using **Python** and [Django Rest
Framework](http://www.django-rest-framework.org). I will show you how to
first create a very basic API, how to handle the authentication and
permissions and I will cover deployment and hosting of images. The full
source code of the tutorial is available
at: <https://github.com/andreagrandi/drf-tutorial>

### Summary of the complete tutorial

1.  Create the basic structure for the API
2.  [Add Authentication and POST
    methods]({filename}creating-a-production-ready-api-with-python-and-django-rest-framework-part-2.md)
3.  [Handling details and changes to existing
    data]({filename}/2017/creating-a-production-ready-api-with-python-and-django-rest-framework-part-3.md)
4.  Testing the API
5.  Switching from Sqlite to PostgreSQL
6.  Hosting the API on Heroku
7.  Add an Image field and save images to S3

Create the basic structure for the API
--------------------------------------

For this tutorial I will assume you have correctly installed at least
**Python** (I will use Python 2.7.x),
[**virtualenv**](https://pypi.python.org/pypi/virtualenv) and
[**virtualenvwrapper**](https://virtualenvwrapper.readthedocs.io/en/latest/)
on your system and I will explain how to create everything else step by
step.

**Note:** at the time of writing, the tutorial has been based on
**Django 1.10.1** and **Django Rest Framework 3.4.7**

### Creating the main project structure

    :::shell
    mkdir drf-tutorial
    mkvirtualenv drf-tutorial
    cd drf-tutorial
    pip install django djangorestframework
    django-admin.py startproject drftutorial .
    cd drftutorial
    django-admin.py startapp catalog

### Data Model

We will create the API for a generic products catalog, using a very
simple structure (to keep things simple). Edit the file
**catalog/models.py** adding these lines:

    :::python
    from __future__ import unicode_literals
    from django.db import models


    class Product(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        price = models.DecimalField(decimal_places=2, max_digits=20)

after creating the model, we need to add 'catalog' application to
**INSTALLED\_APPS**. Edit **settings.py** and add the app at the end of
the list:

    :::python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'catalog',
    ]

at this point the Django application will be recognised by the project
and we can create and apply the schema migration:

    :::shell
    (drf-tutorial) ➜  drftutorial git:(235dfcc) ✗ ./manage.py makemigrations
    Migrations for 'catalog':
        catalog/migrations/0001_initial.py:
            - Create model Product

    (drf-tutorial) ➜  drftutorial git:(235dfcc) ✗ ./manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, catalog, contenttypes, sessions
        Running migrations:
            Applying contenttypes.0001_initial... OK
            Applying auth.0001_initial... OK
            Applying admin.0001_initial... OK
            Applying admin.0002_logentry_remove_auto_add... OK
            Applying contenttypes.0002_remove_content_type_name... OK
            Applying auth.0002_alter_permission_name_max_length... OK
            Applying auth.0003_alter_user_email_max_length... OK
            Applying auth.0004_alter_user_username_opts... OK
            Applying auth.0005_alter_user_last_login_null... OK
            Applying auth.0006_require_contenttypes_0002... OK
            Applying auth.0007_alter_validators_add_error_messages... OK
            Applying auth.0008_alter_user_username_max_length... OK
            Applying catalog.0001_initial... OK
            Applying sessions.0001_initial... OK

### API Serializer

[**Serializers**](http://www.django-rest-framework.org/api-guide/serializers/)
are those components used to convert the received data from JSON format
to the relative Django model and viceversa. Create the new file
**catalog/serializers.py** and place this code inside:

    :::python
    from .models import Product
    from rest_framework import serializers


    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('name', 'description', 'price')

In this case we are using a
[**ModelSerializer**](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer).
We need to create a new class from it, and specify the model attribute,
that's it. In this case we also specify the fields we want to return.

### API View

The serializer alone is not able to respond to an API request, that's
why we need to implement a view. In this first version of the view (that
we will improve soon) we will "manually" transform the data available in
the serializer dictionary to a JSON response. In **catalog/views.py**
add this code:

    :::python
    from django.http import HttpResponse
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser
    from .models import Product
    from .serializers import ProductSerializer


    class JSONResponse(HttpResponse):
        """
        An HttpResponse that renders its content into JSON.
        """
        def __init__(self, data, **kwargs):
            content = JSONRenderer().render(data)
            kwargs['content_type'] = 'application/json'
            super(JSONResponse, self).__init__(content, **kwargs)


    def product_list(request):
        if request.method == 'GET':
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return JSONResponse(serializer.data)

At this point we need to tell our Django app to use this API view when a
certain URL is requested. We first need to add this code in
**catalog/urls.py**

    :::python
    from django.conf.urls import url
    from . import views

    urlpatterns = [
        url(r'^products/$', views.product_list),
    ]

and finally we need to add this to **drftutorial/urls.py**

    :::python
    from django.conf.urls import url, include
    from django.contrib import admin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', include('catalog.urls')),
    ]

#### Testing our work

At this point we should be able to start our Django app:

    :::shell
    ./manage.py runserver

Let's install a tool that will help us to test the API:

    :::shell
    pip install httpie

now we can use it to call our URL:

    :::shell
    $ http http://127.0.0.1:8000/products/
    HTTP/1.0 200 OK
    Content-Type: application/json
    Date: Wed, 28 Sep 2016 09:54:50 GMT
    Server: WSGIServer/0.1 Python/2.7.11
    X-Frame-Options: SAMEORIGIN

    []

It works! It's an empty response of course, because we still don't have
any data to show, but we will see later how to load some example data in
our database. If you have been able to follow the tutorial up to this
point, that's good. If not, don't worry. You can checkout the code at
exactly this point of the tutorial doing:

    :::shell
    git checkout tutorial-1.0

### Improving the API View

There is a quicker and more efficient way of implementing the same API
view we have seen before. We can use a class based view, in particular
the APIView class and also have the JSON response implemented
automatically. Change the code inside **catalog/views.py** with this
one:

    :::python
    from django.http import HttpResponse
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from .models import Product
    from .serializers import ProductSerializer


    class ProductList(APIView):
        def get(self, request, format=None):
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

You will also have to change **catalog/urls.py** in this way:

    :::python
    urlpatterns = [
        url(r'^products/$', views.ProductList.as_view()),
    ]

You can check the source code for this step of the tutorial with:

    :::python
    git checkout tutorial-1.1

There is also another way of writing the same view. Let's try it with
[**ListAPIView**](http://www.django-rest-framework.org/api-guide/generic-views/#listapiview).
Edit **catalog/views.py** again and substitute the code with this one:

    :::python
    from django.http import HttpResponse
    from rest_framework import generics
    from rest_framework.response import Response
    from .models import Product
    from .serializers import ProductSerializer


    class ProductList(generics.ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

With a **ListAPIView** we are basically creating a read-only API that is
supposed to return a list of items. We need to specify a **queryset**
and the **serializer\_class** parameters. Once again, you can get up to
this point, checking out the related git tag:

    :::shell
    git checkout tutorial-1.2

### Creating Initial Data

An API that doesn't return any data is not very useful, right? Also, at
the moment we haven't implemented yet any feature that let us insert any
data. That's why I've created a data migration for you that will insert
some data for you. You may notice that the example data contains some
Italian products... out of the scope of this tutorial, I strongly advise
you to google this products and if you ever happen to visit Italy, try
them. You won't regret!

Going back to our data migration, you first have to create an empty one
with:

    :::shell
    ./manage.py makemigrations --empty catalog

and then open the file that has been created under
**catalog/migrations/** named **0002\_.....** (your name will be
different from mine, so just edit the one starting with 0002 and you
will be fine) and fill it with this code:

    :::python
    from __future__ import unicode_literals
    from django.db import migrations


    def create_initial_products(apps, schema_editor):
        Product = apps.get_model('catalog', 'Product')

        Product(name='Salame', description='Salame Toscano', price=12).save()
        Product(name='Olio Balsamico', description='Olio balsamico di Modena', price=10).save()
        Product(name='Parmigiano', description='Parmigiano Reggiano', price=8.50).save()
        Product(name='Olio', description='Olio Oliva Toscano', price=13).save()
        Product(name='Porchetta', description='Porchetta toscana cotta a legna', price=7.50).save()
        Product(name='Cantucci', description='Cantucci di Prato', price=4).save()
        Product(name='Vino Rosso', description='Vino Rosso del Chianti', price=9.50).save()
        Product(name='Brigidini', description='Brigidini di Lamporecchio', price=3.50).save()


    class Migration(migrations.Migration):

        dependencies = [
            ('catalog', '0001_initial'),
        ]

        operations = [
            migrations.RunPython(create_initial_products),
        ]

to apply the migration we just created, just do:

    :::shell
    ./manage.py migrate

If you try to test the API again from the command line, you will get
these products back:

    :::shell
    $ http http://127.0.0.1:8000/products/
    HTTP/1.0 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Date: Wed, 28 Sep 2016 12:29:36 GMT
    Server: WSGIServer/0.1 Python/2.7.11
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    [
        {
            "description": "Salame Toscano",
            "name": "Salame",
            "price": "12.00"
        },
        {
            "description": "Olio balsamico di Modena",
            "name": "Olio Balsamico",
            "price": "10.00"
        },
        {
            "description": "Parmigiano Reggiano",
            "name": "Parmigiano",
            "price": "8.50"
        },
        {
            "description": "Olio Oliva Toscano",
            "name": "Olio",
            "price": "13.00"
        },
        {
            "description": "Porchetta toscana cotta a legna",
            "name": "Porchetta",
            "price": "7.50"
        },
        {
            "description": "Cantucci di Prato",
            "name": "Cantucci",
            "price": "4.00"
        },
        {
            "description": "Vino Rosso del Chianti",
            "name": "Vino Rosso",
            "price": "9.50"
        },
        {
            "description": "Brigidini di Lamporecchio",
            "name": "Brigidini",
            "price": "3.50"
        }
    ]

Again, you can get up to this point with:

    :::shell
    git checkout tutorial-1.3

### One more thing...

No, we are not going to present a new amazing device, I'm sorry, but I
want to show you a nice Django Rest Framework feature you can have
without much additional work. Edit **settings.py** and add
**rest\_framework** to the list of **INSTALLED\_APPS**:

    :::python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'catalog',
    ]

Now, if you are still running the Django app, try to visit this url from
your browser: <http://127.0.0.1:8000/products/>  
That's very nice, isn't it? You can have browsable APIs at no cost.

### Wrapping Up

I've mentioned at the beginning that this is just the first part of my
API tutorial. In the [next
part]({filename}creating-a-production-ready-api-with-python-and-django-rest-framework-part-2.md)
I will show you how to let the consumer of your API add some products
and leave reviews (we will introduce a new model for this). Also, we
will see how to set proper permissions to these new API methods so that
only admin users will be able to add products while normal users will be
able to add reviews. So, if you feel ready, you can begin to follow the
second part of this
tutorial: [{filename}creating-a-production-ready-api-with-python-and-django-rest-framework-part-2.md]({filename}creating-a-production-ready-api-with-python-and-django-rest-framework-part-2.md)

### References

Some parts of this tutorial and a few examples have been taken directly
from the original [Django Rest Framework
tutorial](http://www.django-rest-framework.org/tutorial/quickstart/).
