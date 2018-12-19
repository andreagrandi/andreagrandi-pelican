Title: Installing Python and virtualenv on OSX
Date: 2018-12-19 15:00
Author: Andrea Grandi
Category: Python
Tags: python, osx, programming, software, development
Slug: installing-python-and-virtualenv-on-osx
Status: published

Every time I need to install Python on OSX or whenever a colleague asks for help, I have to search fo the most updated instructions on Google, and every time I find different ways of doing the exact same thing.

Tired of this, I decided to write down my own notes. Please note that I don't claim this to be the best way of installing Python on OSX. It works fine for me so use it at your own risk.

## Requirements

To follow these instructions you need to at least have installed **brew** on OSX. Please follow the instructions on the official website: [https://brew.sh](https://brew.sh)

## Installing Python 3.7.x and Python 2.7.x

Even if I strongly suggest to start every new project with Python 3 (since Python 2 will only be supported until the end of 2019), there may be use cases when version 2 is still required, so I will give you the instructions to install both.

### Installing Python 3.7.x

    :::text
    brew install python

This will install Python 3 by default.

### Installing Python 2.7.x

    :::text
    brew install python@2

This will install version 2 of Python.

### Add the Python locations to PATH

Edit your `.bashrc` or `.zshrc` and add this:

    :::text
    export PATH="/usr/local/opt/python/libexec/bin:/usr/local/bin:$PATH"

You will need to close your terminal and reopen it for the changes to be applied. Once you have done it, you can verify if Python 3 and Python 2 have been installed correctly:

    :::text
    python --version
    Python 3.7.1

and

    :::text
    python2 --version
    Python 2.7.15

## Install virtualenv and virtualenvwrapper

When working with Python, it's a good thing not to install packages system wide, but confine them in virtual environments. A good and well tested way of doing that is to use `virtualenv` (and its companion `virtualenvwrapper`) which makes the most common operations easier.

    :::text
    pip install virtualenv
    pip install virtualenvwrapper

Those (and only those) two packages will be installed system wide, because we will need them to be available outside of a virtual environment.

### Configure virtualenv

Edit again your `.bashrc` (or `.zshrc`) and add these lines:

    :::text
    export WORKON_HOME=~/.virtualenvs
    [ -f /usr/local/bin/virtualenvwrapper.sh ] && source /usr/local/bin/virtualenvwrapper.sh

This will configure the default location where to store your virtual environments and will run a command every time you open a new terminal, to make sure `virtualenvwrapper` can work correctly.

## Test if the installed tools are working

To make sure everything has been configured correctly, please close and reopen your terminal and let's try to create a new virtual environment:

    :::text
    mkvirtualenv test

which should output something like this:

    :::text
    Using base prefix '/usr/local/Cellar/python/3.7.1/Frameworks/Python.framework/Versions/3.7'
    New python executable in /Users/andrea/.virtualenvs/test/bin/python3.7
    Also creating executable in /Users/andrea/.virtualenvs/test/bin/python
    Installing setuptools, pip, wheel...
    done.
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/get_env_details
    (test) ➜  ~

If you see something similar, it means that the virtual environment has been created correctly. Please note that by default this command will create an environment base on Python 3. Do you need to create one for Python 2? No problem, you just need to do the following:

    :::text
    mkvirtualenv -p /usr/local/bin/python2 test

which should output this:

    :::text
    Running virtualenv with interpreter /usr/local/bin/python2
    New python executable in /Users/andrea/.virtualenvs/test/bin/python2.7
    Also creating executable in /Users/andrea/.virtualenvs/test/bin/python
    Installing setuptools, pip, wheel...
    done.
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/andrea/.virtualenvs/test/bin/get_env_details
    (test) ➜  ~

## Conclusion

That's all you have to do to install and configure Python and virtualenv on OSX. If you have problems, comments or questions, feel free to leave a comment on this post.
