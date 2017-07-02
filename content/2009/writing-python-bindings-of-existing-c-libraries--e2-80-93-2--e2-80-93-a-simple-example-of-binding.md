Title: Writing Python bindings of existing C libraries – (2) – A simple example of binding
Date: 2009-08-06 15:44
Author: admin
Category: HowTo, Igalia, Linux, Maemo (EN), Programmazione, Python
Tags: binding, Igalia, maemo, Python
Slug: writing-python-bindings-of-existing-c-libraries-%e2%80%93-2-%e2%80%93-a-simple-example-of-binding
Status: published

Introduction
------------

As I promised in the preceding post, I'll provide a very easy example of
a python binding. Let's suppose we don't want to use the methods
included in Python to sum two integer values and we want to do it in C
and then call the add method from a python script. I'll write the
complete source code first and then I'll explain all the parts of it.

Source Code
-----------

\[sourcecode language="C"\]  
\#include &lt;Python.h&gt;

static PyObject \*foo\_add(PyObject \*self, PyObject \*args)  
{  
int a;  
int b;

if (!PyArg\_ParseTuple(args, "ii", &a, &b))  
{  
return NULL;  
}

return Py\_BuildValue("i", a + b);  
}

static PyMethodDef foo\_methods\[\] = {  
{ "add", (PyCFunction)foo\_add, METH\_VARARGS, NULL },  
{ NULL, NULL, 0, NULL }  
};

PyMODINIT\_FUNC initfoo()  
{  
Py\_InitModule3("foo", foo\_methods, "My first extension module.");  
}  
\[/sourcecode\]

How it works
------------

First of all we have to include **Python.h** in our C file. This allows
us to write an extension for Python language. To be able to include this
header, we must have the python development packages installed in our
system. For example in Debian based distributions we can install them
with this command:

`sudo apt-get install python2.5-dev`

Every module has at least three parts. In the first part we write
methods we want to call from the final python module: in this case we
have a method called **foo\_add** where "*foo*" is the name of the
module and "*add*" the name of the method. Every method is declared as
**static PyObject**. The method does anything particular except calling
PyArg\_ParseTuple to validate the input (we'll discuss this later),
adding the two passed numbers and returning the result.

In the second part we have something like a dictionary, defined as
static **PyMethodDef** and called foo\_methods (where "foo" again is the
name of the module). For each method we want to expose in our python
module, we have to add something like this:

`{"add", (PyCFunction)foo_add, METH_VARARGS, NULL}`

where "*add*" is the name of the method we want to be visible in our
module, *(PyCFunction)foo\_add* is a pointer to our foo\_add method,
implemented in the C module, METH\_VARARGS means that we want to pass
some parameters to the function and the last one would be the
description of the method (we can leave it NULL if we want).

Third part allows us to register the defined method/s and the module:

`Py_InitModule3("foo", foo_methods, "My first extension module.");`

### Parsing Parameters

The **PyArg\_ParseTuple** function extracts arguments from the
**PyObject** passed as parameter to the current method and follows
almost the sscanf syntax to parse parameters (in this case we had *"ii"*
for two integers). You can fin the complete reference here:
<http://docs.python.org/c-api/arg.html>

Building and installing
-----------------------

To build the module, we have to be in the source directory and execute
this command:

`gcc -shared -I/usr/include/python2.5 foo.c -o foo.so`

then we've to copy the generated module to the python's modules
directory:

`cp foo.so /usr/lib/python2.5/site-packages/`

Testing our module
------------------

Testing the module is really easy. We've to start a python shell or
create a python script with the following source code:

\[sourcecode language="python"\]  
import foo  
print foo.add(2, 3)  
\[/sourcecode\]

if all is working fine, the printed result should be **5**

References
----------

-   <http://docs.python.org/extending/extending.html>
-   <http://www.wrox.com/WileyCDA/WroxTitle/productCd-0764596543.html>

<div id="_mcePaste"
style="overflow: hidden; position: absolute; left: -10000px; top: 399px; width: 1px; height: 1px;">

python2.5-dev

</div>

<div id="_mcePaste"
style="overflow: hidden; position: absolute; left: -10000px; top: 399px; width: 1px; height: 1px;">

python2.5-dev

</div>
