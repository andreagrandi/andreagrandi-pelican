Title: Creating a production ready API with Python and Django Rest Framework – part 4
Date: 2017-08-17 7:00
Author: Andrea Grandi
Category: Development
Tags: API, Django, framework, Python, rest, tutorial
Slug: creating-a-production-ready-api-with-python-and-django-rest-framework-part-4
Status: published

In the [previous
part]({static}/2017/1-creating-a-production-ready-api-with-python-and-django-rest-framework-part-3.md)
of the tutorial we implemented **details** management, **relations**
between models, **nested APIs** and a different level of permissions.
Our API is basically complete but it is working properly? Is the source
code free of bugs? Would you feel confident to refactor the code without
breaking something? The answer to all our question is probably no. **I
can't be sure if the code behaves properly nor I would feel confident
refactoring anything without having some tests coverage**.

As I mentioned previously, we should have written tests since the
beginning, but I really didn't want to mix too many concepts together
and I wanted to let the user concentrate on the Rest Framework instead.

### Test structure and configuration

Before beginning the fourth part of this tutorial, make sure you have
grabbed the latest source code
from <https://github.com/andreagrandi/drf-tutorial> and you have checked
out the previous git tag:

    :::shell
    git checkout tutorial-1.14

Django has an integrated test runner but my personal choice is to use
[**pytest**](https://doc.pytest.org/en/latest/), so as first thing let's
install the needed libraries:

    :::shell
    pip install pytest pytest-django

As long as we respect a minimum of conventions (test files must start
with **test\_** prefix), tests can be placed anywhere in the code. My
advice is to put them all together in a separate folder and divide them
according to app names. In our case we are going to create a folder
named "**tests**" at the same level of **manage.py** file. Inside this
folder we need to create a **\_\_init\_\_.py** file and another folder
called **catalog** with an additional **\_\_init\_\_.py** inside. Now,
still at the same level of **manage.py** create a file called
**pytest.ini** with this content:

    :::python
    [pytest]
    DJANGO_SETTINGS_MODULE=drftutorial.settings

Are you feeling confused? No problem. You can checkout the source code
containing these changes.

    :::shell
    git checkout tutorial-1.15

You can check if you have done everything correctly going inside the
drftutorial folder (the one containing **manage.py**) and launching
**pytest**. If you see something like this, you did your changes
correctly:

    :::shell
    (drf-tutorial) ➜  drftutorial git:(master) pytest
    ============================================================================================================================= test session starts ==============================================================================================================================
    platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
    Django settings: drftutorial.settings (from ini file)
    rootdir: /Users/andrea/Projects/drf-tutorial/drftutorial, inifile: pytest.ini
    plugins: django-3.1.2
    collected 0 items

    ========================================================================================================================= no tests ran in 0.01 seconds =========================================================================================================================
    (drf-tutorial) ➜  drftutorial git:(master)

### Writing the first test

To begin with, I will show you how to write a simple test that will
verify if the API can return the products list. If you remember we
implemented this API in the first part of the tutorial. First of all
create a file called **test\_views.py** under the folder
**drftutorial/tests/catalog/** and add this code:

    :::python
    import pytest
    from django.urls import reverse
    from rest_framework import status
    from rest_framework.test import APITestCase


    class TestProductList(APITestCase):
        @pytest.mark.django_db
        def test_can_get_product_list(self):
            url = reverse('product-list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.json()), 8)

before being able to run this test we need to change a little thing in
the **catalog/urls.py** file, something we should have done since the
beginning. Please change the first url in this way, adding the **name**
parameter:

    :::python
    urlpatterns = [
        url(r'^products/$', views.ProductList.as_view(), name='product-list'),
        ...

at this point we are able to run our test suite again and verify the
test is passing:

    :::shell
    (drf-tutorial) ➜  drftutorial git:(test-productlist) ✗ pytest -v
    ============================================================================================================================= test session starts ==============================================================================================================================
    platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.32, pluggy-0.4.0 -- /Users/andrea/.virtualenvs/drf-tutorial/bin/python2.7
    cachedir: .cache
    Django settings: drftutorial.settings (from ini file)
    rootdir: /Users/andrea/Projects/drf-tutorial/drftutorial, inifile: pytest.ini
    plugins: django-3.1.2
    collected 1 items

    tests/catalog/test_views.py::TestProductList::test_can_get_product_list PASSED

    =========================================================================================================================== 1 passed in 0.98 seconds ===========================================================================================================================

To checkout the source code at this point:

    :::shell
    git checkout tutorial-1.16

### Explaining the test code

When we implement a test, the first thing to do is to create a
**test\_\*** file and import the minimum necessary to write a test class
and method. Each test class must inherit from **APITestCase** and have a
name that start with **Test**, like **TestProductList**. Since we use
[pytest](https://doc.pytest.org/en/latest/), we need to mark our method
with **@pytest.mark.django\_db decorator**, to tell the test suite our
code will explicitly access the database. We are going to use the **client** object
that is integrated in APITestCase to perform the request. Before doing that we
first get the local **url** using Django's **reverse** function. At this point
we do the call using the client:

    :::python
    response = self.client.get(url)

and then we assert a couple of things that we expect to be true:

    :::python
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.json()), 8)

We check that our API returns the **200** status code and that in the returned
JSON there are 8 elements.

It's normally a good practice to create test data inside the tests, but in our case
we previously created a data migration that creates test data. Migrations are
run every time we run tests so when we call our API, the data will be already there.

### Wrapping up

I've written a [few tests](https://github.com/andreagrandi/drf-tutorial/blob/master/drftutorial/tests/catalog/test_views.py) 
for all the views we have implemented until now and they are available
if you checkout this version of the code:

    :::shell
    git checkout tutorial-1.17

I've only tested the views but it would be nice to test even the permission class, for example.
Please remember to write your tests first, if possible: implementing the code will be much more natural
once the tests are already in place.
