Title: Using pyenv and pyenv-virtualenv to install Python and create a virtual environment on MacOS
Date: 2022-01-29 16:00
Author: Andrea Grandi
Category: Development
Tags: python, development, pyenv, virtualenv, pyenv-virtualenv, environment, python310, programming, pip, macos, install, version
Slug: install-python-with-pyenv-and-pyenvvirtualenv-create-virtual-environment-with-specific-python-version-macos
Status: published
Summary: How to use pyenv and pyenv-virtualenv to install a specific version of Python and create a virtual environment with that version on MacOS

This is an update version of my previous tutorial [Install Python with pyenv and pyenv-virtualenv create virtual environment with specific Python version]({filename}/2020/4-install-python-with-pyenv-create-virtualenv.md). In this version I will show how to install Python 3.10.0 and create a virtual environment with that version.

To manage my Python versions I'm using using [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) and once they are correctly configured, it's very easy to install a new Python version.

## Make sure you have the required packages installed

First of all make sure you have all the latest packages installed (I'm using [Homebrew](https://brew.sh) for MacOS):

    :::shell
    brew update
    brew install pyenv
    brew install pyenv-virtualenv

once installed you should see the latest version:

    :::shell
    pyenv --version
    pyenv 2.2.2

## Configure pyenv and pyenv-virtualenv

To be able to use `pyenv` and `pyenv-virtualenv` you need to write this basic configuration in your `~/.bashrc` (or `~/.zshrc` if you are using zsh):

    :::bash
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

## Install Python 3.10.0

To install Python 3.10.0 you only need `pyenv install 3.10.0`:

    :::shell
    pyenv install 3.10.0
    python-build: use openssl@1.1 from homebrew
    python-build: use readline from homebrew
    Downloading Python-3.10.0.tar.xz...
    -> https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
    Installing Python-3.10.0...
    patching file aclocal.m4
    patching file configure
    Hunk #5 succeeded at 10537 (offset -15 lines).
    python-build: use readline from homebrew
    python-build: use zlib from xcode sdk
    Installed Python-3.10.0 to /Users/andrea/.pyenv/versions/3.10.0

## Set Python 3.10.0 as the local version

Now that the version you want has been installed, you need to tell pyenv you want to use it:

    :::shell
    pyenv local 3.10.0
    pyenv which python

which will show you this:

    :::shell
    /Users/andrea/.pyenv/versions/3.10.0/bin/python

## Create a virtual environment using Python from pyenv

To create a virtual environment named `my-310-python` using Python 3.10.0 version, you just need this command:

    :::shell
    pyenv virtualenv 3.10.0 my-310-python

Verify that the virtual environment has been created:

    :::shell
    pyenv virtualenvs
    3.10.0/envs/my-310-python (created from /Users/andrea/.pyenv/versions/3.10.0)

## Test and automatically activate the virtual environment

Create a test folder:

    :::shell
    mkdir test-310

Create a `.python-version` file in the test folder:

    :::shell
    echo my-310-python > test-310/.python-version

Now if you enter the folder (`cd test-310`), the virtual environment will be automatically activated:

    :::shell
    cd test-310
    (my-310-python) ➜  test-310

At this point you can verify that the virtual environment is working, by using `python --version`:

    (my-310-python) ➜  test-310 python --version
    Python 3.10.0
