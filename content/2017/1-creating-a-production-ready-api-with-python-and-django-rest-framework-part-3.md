Title: Creating a production ready API with Python and Django Rest Framework – part 3
Date: 2017-03-12 11:21
Author: Andrea Grandi
Category: Development
Tags: API, Django, framework, Python, rest, tutorial
Slug: creating-a-production-ready-api-with-python-and-django-rest-framework-part-3
Status: published

In the [previous
part]({filename}/2016/creating-a-production-ready-api-with-python-and-django-rest-framework-part-2.md)
we implemented authentication, permissions and the possibility to POST
new products for admins. In this new episode we will see how to
implement **details** management, **relations** between models, **nested
APIs** and a different level of permissions.

If you haven't completed the previous parts or if you want to begin from
this one, checkout the right code first:

    :::shell
    git checkout tutorial-1.10

### Handling Product Details

Our current API methods allow us to list all the products we have in our
catalog and to create a new one (if we have admin permissions), but what
if we wanted to delete or update a single one? What if we wanted to get
only a specific product? We need to handle details.

As first thing we need to change the **ProductSerializer** to return the
id of the product. Edit **catalog/serializers.py** and change the class
in this way:

    :::python
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'description', 'price')

After changing the serializer we need to implement a new view called
**ProductDetail**. Edit **catalog/views.py** and add the following
imports:

    :::python
    from django.http import Http404
    from rest_framework.response import Response
    from rest_framework.views import APIView
    from rest_framework import status

and the following class:

    :::python
    class ProductDetail(APIView):
        def get_object(self, pk):
            try:
                return Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            product = self.get_object(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            product = self.get_object(pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            product = self.get_object(pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

let's connect the new view to the urls, editing catalog/urls.py and
changing the code in this way:

    :::python
    urlpatterns = [
        url(r'^products/$', views.ProductList.as_view()),
        url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    ]

If we try to **PUT**, **DELETE** or **GET** a product like
**/products/1/** we can now update, delete or retrieve an existing item,
but there is a little problem: we haven't set any permission on this
class, so anyone can do it. The previous view was also more compact, why
don't we use a generic view to perform these basic operations? Let's
refactor **ProductDetail** with a
[**RetrieveUpdateDestroyAPIView**](http://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview)
generic class. Open **catalog/views.py** and change the class code in
this way:

    :::python
    class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = (IsAdminOrReadOnly, )

That's it! With just three lines of code we have now implemented the
same feature of the previous class, plus we have set the correct
permissions.

To checkout the code at this point:

    :::shell
    git checkout tutorial-1.12

### Reviews - Relations between models

As many online catalogs already have, it would be nice if our API had an
endpoint where it is possible to leave a review for a product and get a
list of reviews for a specific product. To implement this feature we
need to add a new model to our application. Edit **catalog/models.py**
adding this import:

    :::python
    from django.contrib.auth.models import User

and this Django model:

    :::python
    class Review(models.Model):
        product = models.ForeignKey(Product, related_name='reviews')
        title = models.CharField(max_length=255)
        review = models.TextField()
        rating = models.IntegerField()
        created_by = models.ForeignKey(User)

after creating the model, please remember to create the related DB
**migration**:

    :::shell
    $ ./manage.py makemigrations catalog

When the model is ready, we have to do some changes to the serializers.
First of all we need to write a new one, for our new **Review** model.
Then we have to change our **ProductSerializer** so that it will return
its related reviews. Each Product can have multiple Review. And each
Review will be always linked to a specific Product. Edit
**catalog/serializers.py** and change it in this way:

    :::python
    from .models import Product, Review
    from rest_framework import serializers


    class ReviewSerializer(serializers.ModelSerializer):
        created_by = serializers.ReadOnlyField(source='created_by.username')

        class Meta:
            model = Review
            fields = ('id', 'title', 'review', 'rating', 'created_by')


    class ProductSerializer(serializers.ModelSerializer):
        reviews = ReviewSerializer(many=True, read_only=True)

        class Meta:
            model = Product
            fields = ('id', 'name', 'description', 'price', 'reviews')

**Note:** in **ReviewSerializer** when we serialise the user contained
in **created\_by** field, return the username instead of the id (to make
it more human readable). Another important thing to notice is that the
value of the **related\_name** we have set in the **Review** model must
match with the field name we have added in **ProductSerializer fields**
property. In this case we have set it to **reviews**.

At this point we need to add a new view. Edit **catalog/views.py** and
add the following imports:

    :::python
    from rest_framework.permissions import IsAuthenticatedOrReadOnly
    from .models import Product, Review
    from .serializers import ProductSerializer, ReviewSerializer

then add this class:

    :::python
    class ReviewList(generics.ListCreateAPIView):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer
        permission_classes = (IsAuthenticatedOrReadOnly, )

        def perform_create(self, serializer):
            serializer.save(
                created_by=self.request.user,
                product_id=self.kwargs['pk'])

As you can notice, I had to customise the **perform\_create** method
because the default one doesn't know anything about the fact we want to
set the **created\_by** and **product\_id** fields. Finally we need to
bind this new view to a specific url, so we need to edit
**catalog/urls.py** and add this:

    :::python
    ...
        url(r'^products/(?P<pk>[0-9]+)/reviews/$', views.ReviewList.as_view()),
    ]

At this point any authenticated user should be able to **POST a review**
for a product and anyone should be able to get the **list of reviews**
for each product. If you have any problem with the code and want to move
to this point, please checkout this:

    :::shell
    git checkout tutorial-1.13

### Nested APIs details

To complete our API endpoints for Review, we need to add an additional
feature that will let users to edit/delete their own review. Before
implementing the new view, we need a little bit of refactoring and a new
permission class. Edit **catalog/permissions.py** and add this new
class:

    :::python
    class IsOwnerOrReadOnly(BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in SAFE_METHODS:
                return True

            return obj.created_by == request.user

Basically this will permit changes to the review only to its author. Now
we are going to add new urls and doing some refactoring at the same
time. Edit **catalog/urls.py** and change the urls in this way:

    :::python
    urlpatterns = [
        url(r'^products/$', views.ProductList.as_view()),
        url(r'^products/(?P<product_id>[0-9]+)/$', views.ProductDetail.as_view()),
        url(
            r'^products/(?P<product_id>[0-9]+)/reviews/$',
            views.ReviewList.as_view()
        ),
        url(
            r'^products/(?P<product_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',
            views.ReviewDetail.as_view()
        ),
    ]

You may have noticed that I substituted **pk** with **product\_id**. In
the latest url I added, we need to be able to identify two primary keys:
the one for the product and the one for the review. I renamed the
previous ones for consistency. Now it's time to add the new view for
Review details. Edit **catalog/view.py** and add this class:

    :::python
    class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ReviewSerializer
        permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
        lookup_url_kwarg = 'review_id'

        def get_queryset(self):
            review = self.kwargs['review_id']
            return Review.objects.filter(id=review)

What are we doing here? You may have noticed that we set a new property
called **lookup\_url\_kwarg**. That property is being used to determine
the keyword in **urls.py** to be used for the primary key lookup.

You will also need to do some refactoring to the other views, to adapt
them to the changes we just did to the urls. I suggest you to have a
look at the diffs
here: <https://github.com/andreagrandi/drf-tutorial/compare/tutorial-1.13...tutorial-1.14>
or you can have a look at the whole file
here <https://github.com/andreagrandi/drf-tutorial/blob/541bf31c11fd1dbf2bcc1d31312086995e3e5b48/drftutorial/catalog/views.py>

In alternative, you can fetch the whole source code at this point:

    :::shell
    git checkout tutorial-1.14

### Wrapping Up

In this third part of the tutorial you learned how to handle model
details in the API and how relations between different model work. In
the next part of the tutorial we will do something we should have done
since the beginning: adding tests to our code and learn how to properly
test the API.

### Feedback Please

I know, this blog doesn’t have any “comment” feature (I was tired of
dealing with spam), but if you want to provide some feedback you can
still do it by email. Just visit my
[**About**]({filename}/pages/about.md) page, you will find my
email there.
