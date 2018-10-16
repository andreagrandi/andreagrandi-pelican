Title: Using ipdb with Python 3.7.x breakpoint
Date: 2018-10-16 22:00
Author: Andrea Grandi
Category: Python
Tags: python, debugging, programming, software, development
Slug: using-ipdb-with-python-37-breakpoint
Status: published

Python 3.7.x introduced a [new method to insert a breakpoint](https://docs.python.org/3/whatsnew/3.7.html#pep-553-built-in-breakpoint) in the code.
Before Python 3.7.x to insert a debugging point we had to write ```import pdb; pdb.set_trace()``` which honestly I could never remember (and I also created a snippet on VS Code to auto complete it).

Now you can just write ```breakpoint()``` that's it!

Now... the only problem is that by default that command will use **pdb** which is not exactly the best debugger you can have. I usually use **ipdb** but there wasn't an intuitive way of using it... and no, just installing it in your virtual environment, it won't be used by default.

How to use it then? It's very simple. The new debugging command will read an environment variable named **PYTHONBREAKPOINT**. If you set it properly, you will be able to use ipdb instead of pdb.

    :::text
    export PYTHONBREAKPOINT=ipdb.set_trace

At this point, any time you use `breakpoint()` in your code, **ipdb** will be used instead of **pdb**.

#### References
* https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c
