Title: Creating a production ready API with Python and Django Rest Framework – part 2
Date: 2016-10-01 11:12
Author: Andrea Grandi
Category: Development
Tags: API, Django, framework, Python, rest, tutorial
Slug: creating-a-production-ready-api-with-python-and-django-rest-framework-part-2
Status: published

In the [first
part]({filename}creating-production-ready-api-python-django-rest-framework-part-1.md)
of this tutorial we have seen how to create a basic API using **Django
Rest Framework**. This second part will explain how to implement
**POST** methods and add different levels of **permissions** and
**authentication**. If you are starting from part 2, you may want to
checkout the source code at this exact point:

    :::shell
    git checkout tutorial-1.4

### A step back

Before showing how easy it is to implement a **POST** method for our
existing API, I want to do a step back and show you the "manual way",
using just the
[**APIView**](http://www.django-rest-framework.org/api-guide/views/)
class. Edit the file **catalog/views.py** and change the code in this
way:

    :::python
    from django.http import HttpResponse
    from rest_framework.response import Response
    from rest_framework.views import APIView
    from .models import Product
    from .serializers import ProductSerializer


    class ProductList(APIView):
        def get(self, request, format=None):
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

If we try to use the API again (from the browser of from the http
client), it will still work in the same way. The difference here is that
we are using the very basic **APIView** class and we have explicitly
defined the **GET** method for it.

### Implementing a POST method with APIView

An API is not being used at its full potential if it's read only. We are
going to implement a POST method for the existing view and testing it
with [**httpie**](https://httpie.org/) client again. First of all we
need to add an import to **catalog/views.py**

    :::python
    from rest_framework import status

then we add this method to our **ProductList** class:

    :::python
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

Now let's test our **POST** method we just implemented:

    :::shell
    $ http --json POST http://127.0.0.1:8000/products/ name="Salamino" description="Salamino Piccante" price="10.50"
    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Date: Thu, 29 Sep 2016 11:48:48 GMT
    Server: WSGIServer/0.1 Python/2.7.10
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "description": "Salamino Piccante",
        "name": "Salamino",
        "price": "10.50"
    }

It works! In case something doesn't work, try to fetch the source code
at this point:

    :::shell
    git checkout tutorial-1.7

### Implementing a POST method with ListCreateAPIView

Do you remember when I mentioned at the beginning that there is an easy
way to do the same thing? I wasn't cheating. Let's change again our old
code in **catalog/views.py** but this time we will use a different base
class:

    :::python
    from django.http import HttpResponse
    from rest_framework import generics
    from rest_framework.response import Response
    from .models import Product
    from .serializers import ProductSerializer


    class ProductList(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

let's test this again with **httpie**:

    :::shell
    $ http --json POST http://127.0.0.1:8000/products/ name="Pecorino" description="Pecorino Sardo" price="7.00"
    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Date: Thu, 29 Sep 2016 15:21:20 GMT
    Server: WSGIServer/0.1 Python/2.7.10
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "description": "Pecorino Sardo",
        "name": "Pecorino",
        "price": "7.00"
    }

We just POSTed some data on the API! How can it work? Well, we have
changed the base class from **ListAPIView** to
[**ListCreateAPIView**](http://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview).
This particular class implements **a generic POST method** that will
accept and validate all the fields through the specified serializer.

### Authentication

Now our API let us add products to the catalog, amazing! But... is it
exactly what we want? In a real scenario we don't want any random user
to be able to add products in our database, so we are going to protect
the POST method allowing only Admin users.

Before digging into Django Rest Framework permissions, we need to setup
an authentication system. For simplicity we will implement
[**TokenAuthentication**](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication).
As first step we need to edit **settings.py** and
insert **rest\_framework.authtoken** in the **INSTALLED\_APPS**:

    :::python
        ...
        'rest_framework',
        'rest_framework.authtoken',
        'catalog',
    ]

after this, we need to add **TokenAuthentication** as default
authentication class (append this in **settings.py** at the end):

    :::python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        )
    }

Finally we need to add a particular URL to the project so that clients
will be able to call an endpoint passing **username** and **password**
to get a **token** back. Edit **drftutorial/urls.py** and make it's like
this:

    :::python
    from django.conf.urls import url, include
    from django.contrib import admin
    from rest_framework.authtoken.views import obtain_auth_token

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', include('catalog.urls')),
        url(r'^api-token-auth/', obtain_auth_token),
    ]

Don't forget to re-run the **migrations**, because TokenAuthorization
needs to change a couple of tables:

    :::shell
    $ ./manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, authtoken, catalog, contenttypes, sessions
    Running migrations:
        Applying authtoken.0001_initial... OK
        Applying authtoken.0002_auto_20160226_1747... OK

In case you had any problem changing the code up to this point, you can
always fetch the related git tag:

    :::shell
    git checkout tutorial-1.9

#### Testing the Authentication

Before testing the authentication, make sure you created at least the
Django **superuser** with:

    :::shell
    $ ./manage.py createsuperuser

now let's try to **obtain the token** we will need later for our API
calls:

    :::shell
    $ http --json POST http://127.0.0.1:8000/api-token-auth/ username="yourusername" password="yourpassword"
    HTTP/1.0 200 OK
    Allow: POST, OPTIONS
    Content-Type: application/json
    Date: Fri, 30 Sep 2016 08:55:07 GMT
    Server: WSGIServer/0.1 Python/2.7.11
    X-Frame-Options: SAMEORIGIN

    {
        "token": "bc9514f0892368cfd0ea792a977aff55d53e3634"
    }

We will need to pass this token in every API call we want to be
authenticated. The token is being passed through the "Authentication"
header parameter.

### API Permissions

Authentication is something that identify the user with a particular
system. Permissions instead are the level of things that are allowed or
not allowed for a particular user. In our case we said we want to let
Admin users to be able to POST new products and we want to let even
anonymous users to GET the product list.

Django Rest Framework has some built-in classes that we can apply to our
views to define the level of permissions. We could have used the
[**IsAdminUser**](http://www.django-rest-framework.org/api-guide/permissions/#isadminuser)
class, but it would not allow anonymous users to perform the GET
request. Or we could have used
[**IsAuthenticatedOrReadOnly**](http://www.django-rest-framework.org/api-guide/permissions/#isauthenticatedorreadonly)
class, but this would allow any registered user to add products (and we
want to let only admins).

Or...we can define our own permission class and have exactly what we
want. Create a new file **catalog/permissions.py**

    :::python
    from rest_framework.permissions import BasePermission, SAFE_METHODS


    class IsAdminOrReadOnly(BasePermission):
        def has_permission(self, request, view):
            if request.method in SAFE_METHODS:
                return True
            else:
                return request.user.is_staff

Just as a side note, **SAFE\_METHODS** are **GET**, **HEAD** and
**OPTIONS**. These method are considered "safe" because they don't
change any existing data. Open **catalog/views.py** again, import this
at the beginning:

    :::python
    from .permissions import IsAdminOrReadOnly

and set this as **permission\_classes** to **ProductList**:

    :::python
    ...
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

Let's now try to add a new product using the **token** we got before
(you will have to use your own token of course, mine only works on my
local db):

    :::shell
    $ http --json POST http://127.0.0.1:8000/products/ name="Lardo" description="Lardo di Colonnata" price="8.50" 'Authorization: Token bc9514f0892368cfd0ea792a977aff55d53e3634'
    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Date: Fri, 30 Sep 2016 13:04:13 GMT
    Server: WSGIServer/0.1 Python/2.7.11
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    {
        "description": "Lardo di Colonnata",
        "name": "Lardo",
        "price": "8.50"
    }

It worked! We have now protected our API so that not admin people can't
create any product. If you have any problem with the code, you can check
it out with this tag:

    :::shell
    git checkout tutorial-1.10

### Wrapping Up

We have now implemented the POST method to add new products to our
catalog. In the [next
episode]({filename}/2017/creating-a-production-ready-api-with-python-and-django-rest-framework-part-3.md)
we will see how to implement endpoints to get a single product, to
update or delete products and finally we will allow registered users to
send a review for a specific product.

### Feedback Please

I know, this blog doesn't have any "comment" feature (I was tired of
dealing with spam), but if you want to provide some feedback you can
still do it by email. Just visit my
[**About**]({filename}/pages/about.md) page, you will find my
email there.
