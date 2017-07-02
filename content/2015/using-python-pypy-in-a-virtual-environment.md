Title: Using Python PyPy in a virtual environment
Date: 2015-12-18 17:29
Author: admin
Category: HowTo, Python
Tags: pypy, Python
Slug: using-python-pypy-in-a-virtual-environment
Status: published

Sometimes we need to test if our code also works with
**[PyPy](http://pypy.org/)** implementation of **Python**. Assuming you
have already installed it in your system, first find out where it is
installed:

``` {.lang:zsh .decode:true}
➜  ~  which pypy
/usr/local/bin/pypy
```

then you need **mkvirtualenv** to create a virtual environment that will
use this runtime:

``` {.lang:zsh .decode:true}
➜  ~  mkvirtualenv -p /usr/local/bin/pypy pypy-test
Running virtualenv with interpreter /usr/local/bin/pypy
New pypy executable in pypy-test/bin/pypy
Installing setuptools, pip, wheel...done.
(pypy-test)➜  ~  python
Python 2.7.10 (f3ad1e1e1d6215e20d34bb65ab85ff9188c9f559, Sep 01 2015, 06:26:30)
[PyPy 2.6.1 with GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>>
```

That's it! You can now use this virtual environment to run your Python
application using PyPy environment.
