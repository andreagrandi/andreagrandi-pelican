Title: Writing Python bindings of existing C libraries – (3) – Building and Installing with distutils
Date: 2009-08-13 10:39
Author: admin
Category: HowTo, Igalia, Linux, Maemo (EN), Programmazione, Python
Tags: binding, distutils, library, maemo, Python, setup
Slug: writing-python-bindings-of-existing-c-libraries-%e2%80%93-3-%e2%80%93-building-and-installing-with-distutils
Status: published

In the last post of this series, we saw how to write a simple binding
and we finished to build and install it manually. This is of course not
a good way to manage the building/installation procedure.

In Python we can use a library called **distutils** that let us to
automatize the building and installing process. I'll use the **foo**
source code to create the package, so it will be easier to understand.

Using distutils
---------------

All we have to do is to write a **setup.py** file similar to this one:

\[sourcecode lang="python"\]  
from distutils.core import setup, Extension

foomodule = Extension('foo', sources = \['foo.c'\])

setup (name = 'Foo',  
version = '1.0',  
description = 'This is a package for Foo',  
ext\_modules = \[foomodule\])  
\[/sourcecode\]

As you can see, we have to first import needed modules with: **from
distutils.core import setup, Extension**  
then we create an entry for each module we have (in this case just one,
"foomodule"). We then call the **setup()** method passing it all the
parameters and our **setup.py** is complete.

Building and installing
-----------------------

To test it we can try to build the package in this way:

`python2.5 setup.py build`

if we want to install the module in our system:

`python2.5 setup.py install`

References
----------

-   Official Python documentation:
    <http://docs.python.org/extending/building.html>

