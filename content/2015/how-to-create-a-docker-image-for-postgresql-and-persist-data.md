Title: How to create a Docker image for PostgreSQL and persist data
Date: 2015-02-21 20:24
Author: admin
Category: DevOps, Docker, HowTo, Linux, PostgreSQL
Tags: containers, devops, docker, fig, Linux, OSX, postgresql
Slug: how-to-create-a-docker-image-for-postgresql-and-persist-data
Status: published

Before I start, let me confirm to you that official
[**Docker**](https://www.docker.com/) images for
[**PostgreSQL**](http://www.postgresql.org/) already exist and are
available here: <https://registry.hub.docker.com/_/postgres/> so this
howto wants to be a guide to explain how to create these images and talk
about some of the Docker features.

I will assume that you have already installed Docker on your machine. I
have tested these instructions both on **Ubuntu Linux** and **OSX** (OSX
users will need to install [boot2docker](http://boot2docker.io/),
instructions are not available in this guide).

Dockerfile
----------

To create a Docker image we need to create a text file named
**Dockerfile** and use the available commands and syntax to declare how
the image will be built. At the beginning of the file we need to specify
the base image we are going to use and our contact informations:

``` {.theme:github .decode-attributes:false .tab-convert:true .lang:default .decode:true}
FROM ubuntu:14.04
MAINTAINER Andrea Grandi <nospamthanks@gmail.com>
```

In our case we are using **Ubuntu 14.04** as base image. After these
instructions we need to add PostgreSQL package repository and GnuPG
public key:

``` {.theme:github .decode-attributes:false .lang:default .decode:true}
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
```

then we need to update the packages available in Ubuntu and install
PostgreSQL:

``` {.theme:github .decode-attributes:false .lang:default .decode:true}
RUN apt-get update && apt-get -y -q install python-software-properties software-properties-common   
   && apt-get -y -q install postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3
```

We are installing version 9.3 of PostgreSQL, instructions would be very
similar for any other version of the database.

**Note:** it's important to have **apt-get update** and **apt-get
install** commands in the same **RUN** line, else they would be
considered two different layers by Docker and in case an updated package
is available it won't be installed when the image is rebuilt.

At this point we switch to **postgres** user to execute the next
commands:

``` {.theme:github .lang:default .decode:true}
USER postgres
RUN /etc/init.d/postgresql start   
   && psql --command "CREATE USER pguser WITH SUPERUSER PASSWORD 'pguser';"   
   && createdb -O pguser pgdb
```

We switch to **root** user and we complete the configuration:

``` {.theme:github .lang:default .decode:true}
USER root
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf
```

We expose the port where PostgreSQL will listen to:

``` {.theme:github .lang:default .decode:true}
EXPOSE 5432
```

We setup the data and shared folders that we will use later:

``` {.theme:github .lang:default .decode:true}
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
```

Finally we switch again to the **postgres** user and we define the entry
command for this image:

``` {.theme:github .lang:default .decode:true}
USER postgres
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
```

The full **Dockerfile** is available
here <https://github.com/andreagrandi/postgresql-docker/blob/master/Dockerfile>

Building Docker image
---------------------

Once the Dockerfile is ready, we need to build the image before running
it in a container. Please customize the tag name using your own
docker.io hub account (or you won't be able to push it to the hub):

``` {.theme:github .lang:default .decode:true}
docker build --rm=true -t andreagrandi/postgresql:9.3 .
```

Running the PostgreSQL Docker container
---------------------------------------

To run the container, once the image is built, you just need to use this
command:

``` {.theme:github .lang:default .decode:true}
docker run -i -t -p 5432:5432 andreagrandi/postgresql:9.3
```

Testing the running PostgreSQL
------------------------------

To test the running container we can use any client, even the
commandline one:

``` {.theme:github .lang:default .decode:true}
psql -h localhost -p 5432 -U pguser -W pgdb
```

When you are prompted for password, type: **pguser**  
Please note that **localhost** is only valid if you are running Docker
on Ubuntu. If you are an OSX user, you need to discover the correct ip
using: **boot2docker ip**

Persisting data
---------------

You may have noticed that once you stop the container, if you previously
wrote some data on the DB, that data is lost. This is because by default
Docker containers are not persistent. We can resolve this problem using
a data container. My only suggestion is not to do it manually and use a
tool like [**fig**](http://www.fig.sh/) to orchestrate this. Fig is a
tool to orchestrate containers and its features are being rewritten in
Go language and integrated into Docker itself. So if you prepare a
**fig.yml** configuration file now, you will be able, hopefully, to
reuse it once this feature will be integrated into Docker. Please refer
to fig website for the instructions to install it (briefly: under Ubuntu
you can use **pip install fig** and under OSX you can use **brew install
fig**).

``` {.theme:github .lang:default .decode:true}
dbdata:
  image: andreagrandi/postgresql:9.3
  volumes:
    - /var/lib/postgresql
  command: true

db:
  image: andreagrandi/postgresql:9.3
  volumes_from:
    - dbdata
  ports:
    - "5432:5432"
```

Save this file as **fig.yml** in the same folder of the Dockerfile and
spin up the container using this command: **fig up**

``` {.theme:github .lang:default .decode:true}
andreas-air:postgresql-docker andrea [master] $ fig up
Recreating postgresqldocker_dbdata_1...
Recreating postgresqldocker_db_1...
Attaching to postgresqldocker_db_1
db_1 | 2015-02-21 19:01:07 UTC [6-1] LOG:  database system was interrupted; last known up at 2015-02-21 17:46:10 UTC
db_1 | 2015-02-21 19:01:07 UTC [6-2] LOG:  database system was not properly shut down; automatic recovery in progress
db_1 | 2015-02-21 19:01:07 UTC [6-3] LOG:  redo starts at 0/1782F68
db_1 | 2015-02-21 19:01:07 UTC [6-4] LOG:  record with zero length at 0/1782FA8
db_1 | 2015-02-21 19:01:07 UTC [6-5] LOG:  redo done at 0/1782F68
db_1 | 2015-02-21 19:01:07 UTC [6-6] LOG:  last completed transaction was at log time 2015-02-21 17:46:10.61746+00
db_1 | 2015-02-21 19:01:07 UTC [1-1] LOG:  database system is ready to accept connections
db_1 | 2015-02-21 19:01:07 UTC [10-1] LOG:  autovacuum launcher started
```

If you try to write some data on the database and then you stop (CTRL+C)
the running containers and spin up them again, you will see that your
data is still there.

Conclusion
----------

This is just an example of how to prepare a Docker container for a
specific service. The difficoult part is when you have to spin up
multiple services (for example a Django web application using
PostgreSQL, RabbitMQ, MongoDB etc...), connect them all together and
orchestrate the solution. I will maybe talk about this in one of the
next posts. You can find the full source code of my PostgreSQL Docker
image, including the fig.yml file in this
repository <https://github.com/andreagrandi/postgresql-docker>
