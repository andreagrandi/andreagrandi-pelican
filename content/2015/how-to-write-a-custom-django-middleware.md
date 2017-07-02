Title: How to write a custom Django Middleware
Date: 2015-08-23 21:46
Author: admin
Category: Django, HowTo, Programmazione, Python
Tags: Django, HowTo, middleware, Python, tutorial
Slug: how-to-write-a-custom-django-middleware
Status: published

To understand how a **[Django
Middleware](https://docs.djangoproject.com/en/1.8/topics/http/middleware/)**
works we need to remember that the basic architecture of Django is
composed by a **request** and a **response**. A middleware is something
that stays in the middle. Let's give a look to the next diagram, taken
from official Django documentation:

[![middleware](https://www.andreagrandi.it/wp-content/uploads/2015/08/middleware.png){.aligncenter
.size-full .wp-image-1012 width="601"
height="511"}](https://www.andreagrandi.it/wp-content/uploads/2015/08/middleware.png)

 

Important things to know
------------------------

There are four important things to know about middlewares:

-   You need to write a class that just inherit from ***object***
-   The **order** where you place your middleware in **settings.py** is
    important: middlewares are processed from top to bottom during a
    request and from bottom to top during a response.
-   You don't need to implement all the available methods of a
    middleware. For example you can just implement **process\_request**
    and **process\_template\_response**
-   If you implement **process\_request** and you decide to return an
    **HttpResponse**, all the other middlewares, views etc... will be
    ignored and only your response will be returned

Writing a middleware
--------------------

In my example I wanted to implement a feature that saves the time when a
request is made and the time when a request has been processed, then
calculates the time delta and exposes this value in the context so that
is accessible from our templates. How to implement a similar feature
using a middleware? Here is my example:

``` {.lang:python .decode:true}
from datetime import datetime


class BenchmarkMiddleware(object):
    def process_request(self, request):
        request._request_time = datetime.now()

    def process_template_response(self, request, response):
        response_time = request._request_time - datetime.now()
        response.context_data['response_time'] = abs(response_time)
        return response
```

Please don't care about how I calculated the time. I'm aware that there
are better ways to do it, but I just wanted to keep it simple and show
how to implement a simple middleware.

If you want to see a **complete example** of a project that includes and
uses this middleware, here you can find the complete source
code: <https://github.com/andreagrandi/benchmark-middleware-example>

References
----------

-   <https://docs.djangoproject.com/en/1.8/topics/http/middleware/>
-   <http://agiliq.com/blog/2015/07/understanding-django-middlewares/>
-   <http://code.runnable.com/UrSGolK00ygpAAAQ/creating-a-custom-middleware-for-python-and-django>

