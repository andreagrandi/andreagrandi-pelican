Title: Automatically pull updated Docker images and restart containers with docker-puller
Date: 2014-10-25 10:56
Author: admin
Category: HowTo, Linux
Tags: containers, docker, docker.io, Flask, Python
Slug: automatically-pull-updated-docker-images-and-restart-containers-with-docker-puller
Status: published

If you use [docker.io](http://docker.io) (or any similar service) to
build your **Docker** containers, it may be possible that, once the new
image is generated, you want your Docker host to automatically pull it
and restart the container.

Docker.io gives you the possibility to set a **web hook** after a
successful build. Basically it does a POST on a defined URL and send
some informations in JSON format.

[docker-puller](https://github.com/glowdigitalmedia/docker-puller)
listens to these web hooks and can be configured to run a particular
script, given a specific hook. It's a very simple service I wrote using
Python/Flask. It's also my first Flask application, so if you want to
improve it, feel free to send me a pull request on GitHub.

**Note:** this is not the only existing service that is able to do this
task. I took inspiration from this
article <http://nathanleclaire.com/blog/2014/08/17/automagical-deploys-from-docker-hub/>
and I really tried to
customize <https://github.com/cpuguy83/dockerhub-webhook-listener> for
my own needs, but the problem is that **dockerhub-webhook-listener** is
not ready to be used as is (you have to customize it) and I'm not very
good with **Golang** (yet) to be able to do it in little time. This is
why I rewrote the service in Python (that is my daily language). I want
to thank [Brian Goff](https://github.com/cpuguy83) for the idea and all
the people in **\#docker @ FreeNode** for the support.

How to use docker-puller {#how-to-use-docker-puller style="color: #333333;"}
------------------------

Setting up the service should be quite easy. After you clone the
repository from https://github.com/glowdigitalmedia/docker-puller there
is a **config.json** file where you define the **host**, **port**, a
**token** and a list of **hooks** you want to react to. For example:

    {
        "host": "localhost",
        "port": 8000,
        "token": "abc123",
        "hooks": {
            "hello": "scripts/hello.sh"
        }
    }

Create a **bash script** (in this case it was called hello.sh) and put
it under script folder and write the instructions to be executed to pull
the new image and restart the container (example):

    docker pull andreagrandi/test:latest
    docker stop test
    docker rm test
    docker run --name test -d -p 8000:80 andreagrandi/test:latest

Once configured, I suggest you to setup a **Nginx** entry (instructions
not covered here) that for example redirect
**yourhost.com/dockerpuller** to **localhost:8000** (I would advise to
enable SSL too, or people could be able to sniff your token). The
service can be started with: "**python app.py**" (or you can setup a
Supervisor script).

At this point docker-puller is up and running. Go to **docker.io**
automatic build settings and setup a webhook like this:
**http://yourhost.com/dockerpuller?token=abc123&hook=hello**

Every time docker.io finishes building and pushing your image to the
docker registry, it will **POST** on that URL. docker-puller will catch
the POST, check for a valid token, get the hook name and will execute
the relative script.

That's all! I hope this very simple service can be useful to other
people and once again, if you want to improve it, I will be glad to
accept your pull requests on GitHub.
