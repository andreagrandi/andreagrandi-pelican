Title: Using virtualenv to manage multiple Python/Django environments in the same machine
Date: 2013-04-25 22:58
Author: admin
Category: HowTo, Linux, Programmazione, Python, Ubuntu (EN)
Tags: Django, Python, virtualenv
Slug: using-virtualenv-to-manage-multiple-pythondjango-environments-in-the-same-machine
Status: published

Developing Python applications sometimes it's useful to be able to test
the code with different environments, for example a particular version
of Python or a specific Django version etc... Setting up many different
virtual machines would be really too much work and even using a chroot
environment is not what you need in some cases. Thanks to
[**virtualenv**](https://github.com/pypa/virtualenv) is it possible to
create a self contained Python environment with all the specific
libraries you may need. Using virtualenv is very easy:

-   Creating the virtual environment: **virtualenv
    myenv --no-site-packages**
-   Entering the virtual environment: **source myenv/bin/activate**
-   Deactivating the virtual environment: **deactivate**

That's it! Once you're inside the virtual environment you will be using
the Python libraries inside it. I suggest you to install all the Python
libraries you need using [**pip**](https://pypi.python.org/pypi/pip).
