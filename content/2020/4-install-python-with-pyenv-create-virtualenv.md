Title: Using pyenv to install Python and create a virtual environment
Date: 2020-10-10 19:00
Author: Andrea Grandi
Category: Development
Tags: python, development, pyenv, virtualenv, mkvirtualenv, environment, python39, programming, python3, pip, macos, install, version
Slug: install-python-with-pyenv-create-virtual-environment-with-specific-python-version
Status: published
Summary: How to use pyenv to install a specific version of Python and create a virtual environment with that version

A few days ago [Python 3.9.0](https://docs.python.org/3/whatsnew/3.9.html) has been released and I really wanted to test ist latest features (maybe I will do a 
separate post to talk about them) without messing my system with another Python version.

To manage my Python versions I've been using [pyenv](https://github.com/pyenv/pyenv) for a while and once configured, it's very easy to install a new Python version.

## Make sure your pyenv is updated

You should have at least **pyenv 1.2.21** if you want to test Python 3.9.0
In case you haven't updated it and you are using MacOS, you can do it with this command:

    :::shell
    brew update && brew upgrade pyenv

once installed you should see the latest version:

    :::shell
    pyenv --version
    pyenv 1.2.21

## Install Python 3.9.0

To install Python 3.9.0 you only need `pyenv install 3.9.0`:

    :::shell
    pyenv install 3.9.0
    python-build: use openssl@1.1 from homebrew
    python-build: use readline from homebrew
    Downloading Python-3.9.0.tar.xz...
    -> https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
    Installing Python-3.9.0...
    python-build: use readline from homebrew
    python-build: use zlib from xcode sdk
    Installed Python-3.9.0 to /Users/andrea/.pyenv/versions/3.9.0

## Set Python 3.9.0 as the local version

Now that the version you want has been installed, you need to tell pyenv you want to use it:

    :::shell
    pyenv local 3.9.0
    pyenv which python
    /Users/andrea/.pyenv/versions/3.9.0/bin/python

## Install virtualenvwrapper for pyenv

pyenv needs its own installation of **virtualenvwrapper** to manage virtualenvs. 
You can configure it using `pyenv virtualenvwrapper`:

    :::shell
    pyenv virtualenvwrapper
    Collecting virtualenvwrapper
    Using cached virtualenvwrapper-4.8.4.tar.gz (334 kB)
    Collecting virtualenv
    Downloading virtualenv-20.0.33-py2.py3-none-any.whl (4.9 MB)
        |████████████████████████████████| 4.9 MB 4.1 MB/s
    Collecting virtualenv-clone
    Using cached virtualenv_clone-0.5.4-py2.py3-none-any.whl (6.6 kB)
    Collecting stevedore
    Downloading stevedore-3.2.2-py3-none-any.whl (42 kB)
        |████████████████████████████████| 42 kB 2.7 MB/s
    Collecting six<2,>=1.9.0
    Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
    Collecting filelock<4,>=3.0.0
    Using cached filelock-3.0.12-py3-none-any.whl (7.6 kB)
    Collecting distlib<1,>=0.3.1
    Using cached distlib-0.3.1-py2.py3-none-any.whl (335 kB)
    Collecting appdirs<2,>=1.4.3
    Using cached appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
    Collecting pbr!=2.1.0,>=2.0.0
    Using cached pbr-5.5.0-py2.py3-none-any.whl (106 kB)
    Using legacy 'setup.py install' for virtualenvwrapper, since package 'wheel' is not installed.
    Installing collected packages: six, filelock, distlib, appdirs, virtualenv, virtualenv-clone, pbr, stevedore, virtualenvwrapper
        Running setup.py install for virtualenvwrapper ... done
    Successfully installed appdirs-1.4.4 distlib-0.3.1 filelock-3.0.12 pbr-5.5.0 six-1.15.0 stevedore-3.2.2 virtualenv-20.0.33 virtualenv-clone-0.5.4 virtualenvwrapper-4.8.4

## Create a virtual environment using Python from pyenv

At this point you can create the virtual environment based on Python 3.9.0 using this command `mkvirtualenv -p $(pyenv which python) py39-test`:

    :::shell
    mkvirtualenv -p $(pyenv which python) py39-test
    created virtual environment CPython3.9.0.final.0-64 in 1394ms
    creator CPython3Posix(dest=/Users/andrea/.virtualenvs/py39-test, clear=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/andrea/Library/Application Support/virtualenv)
        added seed packages: pip==20.2.3, setuptools==50.3.0, wheel==0.35.1
    activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/py39-test/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/py39-test/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/py39-test/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/py39-test/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/py39-test/bin/get_env_details

## Check you are using the correct Python version

    :::shell
    (py39-test) ➜  ~ python --version
    Python 3.9.0

As you can see from the above output, we have created a new `virtualenv` using **Python 3.9.0** which has been installed through `pyenv`.
