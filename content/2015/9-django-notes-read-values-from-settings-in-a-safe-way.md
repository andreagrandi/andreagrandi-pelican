Title: Django Notes: read values from settings in a safe way
Date: 2015-08-29 15:50
Author: admin
Category: Django, HowTo, Programmazione, Python
Tags: Django, getattr, Python, settings
Slug: django-notes-read-values-from-settings-in-a-safe-way
Status: published

Working on **Django** projects I find very often that many developers
access the values that are defined in **settings** in this way

``` {.lang:python .decode:true}
from django.conf import settings

my_value = settings.MY_SETTING
```

What happens if **MY\_SETTING** has not been defined in **settings.py**?
The code will raise an error and crash, of course. How can we make the
code more reliable? We could *try/except* the code block that tries to
read the value and maybe set a value if we get an exception, but this
would not be a clean way to do this job.

A cleaner way to do it is to use **getattr** in this way:

``` {.lang:python .decode:true}
from django.conf import settings

my_value = getattr(settings, 'MY_SETTING', 'my-default-value')
```

**getattr** will try to read **MY\_SETTING** value from **settings.py**,
if the value doesn't exist **my\_value** will be assigned with
**my-default-value**.
