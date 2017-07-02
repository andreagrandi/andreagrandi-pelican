Title: Writing Python bindings of existing C libraries - (1) - Introduction
Date: 2009-08-03 10:04
Author: admin
Category: HowTo, Igalia, Linux, Maemo (EN), Programmazione, Python
Tags: bindings, C, Igalia, libraries, library, maemo, pymaemo, Python
Slug: writing-python-bindings-of-existing-c-libraries-1-introduction
Status: published

This summer I'm having the pleasure of working in
[**Igalia**](http://www.igalia.com) (a spanish free software company)
for a couple of months and they assigned me to an interesting project:
developing **Python bindings** for **MAFW** library (a **Maemo**
multimedia library that will be used in **Fremantle** release).

Having the opportunity to work both with **C** (yes, Python bindings are
almost C code) and **Python** (it's a good practice to write unittest of
all implemented methods) it's a good way to improve my knowledges in
both languages and since I wasn't able to find much documentation about
these kind of things, I'm going to share my own experiences.

**What is a Binding?**

A binding is a Python module, written in C language, that allows Python
developers to call functions from existing C libraries from their python
applications. It's just like a "*bridge*" from C world to Python one.

**Why writing bindings?**

There are a couple of reasons to write python bindings instead of
writing a library in python language from scratch.

First of all I don't think is good duplicating code, so if a library
already exists and it's written in C, why writing it again in another
language? There's no reason. A lot of code already exist in C world and
all we have to do is to create a bridge with python world.

Another good reason, in particular when a C library doesn't exist yet,
is the fact that python code is slower than C code for some tasks (for
example multimedia codecs). In these cases is good to implement the core
library in C language and then create a python binding for it.

**Coming next**

As the title of this post says, this is only an introduction to the
subjects I'm going to write about. If you have any particular request
about any argument you would like to read, please feel free to leave me
a comment. Next posts will talk about these things:

-   **A simple example of binding:** I'll write a simple library in C
    language and I'll show how to create the relative python binding,
    providing complete source code and an example for python developers.
-   **Building and installing python bindings with distutils:** I'll
    explain how to use **distutils** to build and install the binding
    (using the well know method "python setup.py install").
-   **Defining new types:** this post will be about how to write new
    types in C language and being able to use them from python code.
-   **Using codegen to write bindings:** I'll explain how to use
    **codegen** utils to automate lot of tasks, to generate the most
    part of binding code and how to customize the generated code using
    overrides.

