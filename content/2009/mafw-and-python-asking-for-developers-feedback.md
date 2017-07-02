Title: MAFW and Python: asking for developers feedback
Date: 2009-08-05 10:16
Author: admin
Category: Igalia, Linux, Maemo (EN), Programmazione, Python
Tags: bindings, fremantle, maemo, mafw, Python
Slug: mafw-and-python-asking-for-developers-feedback
Status: published

MAFW is a new multimedia framework that will be used in Fremantle.

The PyMaemo team is currently working on writing bindings for Python  
language for this library and at the moment we've released a 0.1  
version of python-mafw that you can install directly from Scratchbox  
repository.

Not all the methods are implemented (you can manage the Registry and  
the Playlist, but nothing more), because even if we're using codegen  
to generate bindings (and it's helping us a lot), we've seen that at  
least 30-40 methods have to be overridden by hand so it's taking us  
more time than we expected and we're trying to organize how to  
continue this work.

We would like to get feedback from python application developers and  
also from C application developers that are currently using MAFW so we  
can work on a "roadmap" that reflects what developers want:

-   What are the functionalities you're using in your application that
    you think they cannot miss in the Python binding?
-   Have you already started using MAFW or even better python-mafw to
    develop something?
-   What is the currently missing method/methods you would like to be
    implemented first?

Come on developers! We're waiting for your feedback :)
