Title: How to publish a Python package to PyPI
Date: 2016-04-10 19:05
Author: Andrea Grandi
Category: Development
Tags: pip, pypi, Python
Slug: how-to-publish-a-python-package-to-pypi
Status: published

**PyPI** is the **Python Package Index**, that archive that let you
install a package using pip, for example: **pip install Flask**

In the past days I started writing a **Python API client** for
**[Toshl](https://www.toshl.com)** expense manager and I decided to
publish the library on PyPI. You can have a look at my library
here <https://github.com/andreagrandi/toshl-python> (please note: it's
still in development and [Toshl API](https://developer.toshl.com/) is
not even public yet) in case you are not sure how to structure it.

I found a [nice
guide](http://peterdowns.com/posts/first-time-with-pypi.html) but it
wasn't complete (for example it didn't say how to sign packages) so I
decided to rewrite it adding more information.

### Create PyPI accounts

To publish packages on PyPI you need to create two accounts: one for the
[production server](http://pypi.python.org/pypi?%3Aaction=register_form)
and another one for the [test
server](http://testpypi.python.org/pypi?%3Aaction=register_form). When
you register, please specify (if you have one, but I really hope you do)
the **PGP** id of your public key. Once the accounts are created, you
need to create a file named **.pypirc** in your \$HOME folder containing
the following configuration:

    :::shell
    [distutils]
    index-servers =
    pypi
    pypitest

    [pypi]
    repository=https://pypi.python.org/pypi
    username=your_username
    password=your_password

    [pypitest]
    repository=https://testpypi.python.org/pypi
    username=your_username
    password=your_password

Please substitute **your\_username** and **your\_password** with the
details you sent during the registration.

### Preparing the package

I assume you have structured your library in the proper way and have
included a **setup.py** with all the configuration (it's not something
specific to PyPI so you should have done it already). If you haven't I
remember you can give a look at my library
here <https://github.com/andreagrandi/toshl-python> in particular to the
**setup.py**:

    :::python
    from setuptools import setup, find_packages

    setup(
        name='toshl',
        version='0.0.3',
        url='https://github.com/andreagrandi/toshl-python',
        download_url='https://github.com/andreagrandi/toshl-python/tarball/0.0.3',
        author='Andrea Grandi',
        author_email='a.grandi@gmail.com',
        description='Python client library for Toshl API.',
        packages=find_packages(exclude=['tests']),
        zip_safe=False,
        include_package_data=True,
        platforms='any',
        license='MIT',
        install_requires=[
            'requests==2.9.1',
        ],
    )

### Upload the package to PyPI Test server

The first time you upload the package you will need to register it:

    :::shell
    python setup.py register -r pypitest

and then you will need to build the package and upload it (please note
I'm using the **--sign** to sign the package with PGP):

    :::shell
    python setup.py sdist upload --sign -r pypitest

### Upload the package to PyPI production server

Once you have verified that you are able to build and upload the package
to the test server (without getting any errors), you should upload it to
the production server:

    :::shell
    python setup.py register -r pypi
    python setup.py sdist upload --sign -r pypi

This is everything you need to do if you want to publish a Python
package on PyPI. Happy coding!
