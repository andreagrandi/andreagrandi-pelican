Title: Set specific environment variables activating a Python virtual environment
Date: 2020-10-16 21:00
Author: Andrea Grandi
Category: Development
Tags: set, environment, variables, activate, python, virtual, terminal, bash, zsh, env, dotenv, script
Slug: set-specific-environment-variables-activating-python-virtual-environment
Status: published
Summary: How to set specific environment variables when we activate a Python virtual environment

When using Python virtual environments it can be useful to have certain **environment variables** automatically set when we activate it.
For example we can have a projects that needs to connect to a database or we may need specific settings to run a service. 
Automating this process makes sure we don't forget about setting everything we need.

## Storing the configuration

I strongly suggest to store all the configuration in the root of your project in a file named `.env` which you need to take care of adding to your `.gitignore`.

An example of `.env` file:

    :::bash
    MY_USERNAME=user1
    MY_PASSWORD=secret
    MY_SERVICE_URL=http://localhost:5000

## How to activate the configuration

Python virtual environments have a few scripts that are beign executed in certain situations. In particular there is one named `postactivate` that is being run after you activate trhe virtual environment.

You need to first find the folder where it's located and to do this, you need to first **activate your virtual environment**. Now you need to run `cdvirtualenv` in your terminal and your working directory will be set to where the virtual environment is located.

At this point edit `postactivate` file with (you can replace `nano` with your preferred editor) `nano bin/postactivate` and add the following script:

    :::bash
    #!/bin/zsh
    # This hook is sourced after this virtualenv is activated.
    set -a
    source .env
    set +a

**Note:** I'm using `zsh` here but you can replace it with `bash` (the syntax should be the same).

## Test the configuration

To make the configuration effective you need to `deactivate` your virtual environment and `activate` it again. The `postactivate` script will run automatically and you can now check that your environment variables have been set correctly (the `...` have been placed to replace other existing values):

    :::shell
    (test-env) ➜ env
    ...
    MY_USERNAME=user1
    MY_PASSWORD=secret
    MY_SERVICE_URL=http://localhost:5000

As you can see the values configured in the `.env` file have been correctly set.
