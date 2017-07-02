Title: Django Notes: tests, setUp method and db data
Date: 2015-07-23 22:41
Author: admin
Category: Django, Python
Slug: django-notes-tests-setup-method-and-db-data
Status: published

This won't be a full post, but just a quick note (probably the first one
of a serie) about development with Django.

When we write a **TestCase** test, if we have defined a **setUp**
method, it will be called before the execution of each test. One could
think that the database is completely reset after each test, but this is
not true (not like I was thinking). After each test, whatever we wrote
on the database is rolled back. If we create a "Client" row (assuming we
have a model called Clients) in our setUp, when we call it the second
time the ID won't be 1 as someone (me included) could expect. It will be
2 instead, because the database has not completely deleted and created
from scratch.

This means that we can't assume that our Client ID will always be 1 for
each test and we should rather reference to it in a dinamic way like:
**self.client.id**

This could be a trivial thing for many people but I was not 100% sure
about this so I asked for a confirmation on **\#django** IRC room and
people (expecially **apollo13**) was kind enough to explain me how it
works.
