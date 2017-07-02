Title: Using Cloud9 IDE to develop Django applications
Date: 2013-01-05 15:20
Author: admin
Category: HowTo, Programmazione, Python, Ubuntu (EN)
Slug: using-cloud9-ide-to-develop-django-applications
Status: published

[Django](https://www.djangoproject.com/) is becoming very popular for
dynamic websites development (actually it already is) so I decided to
start learning it, with the help of a [good
book](http://www.apress.com/9781430219361). To develop Django web
applications you need a good IDE and an environment that support at
least Python and a database (SQL Lite, MySQL etc...). If you have
multiple machines and you alternate from multiple operating systems, the
best thing is using an environment that you can use everywhere, from
your favourite browser.

Here comes [**Cloud9**](https://c9.io), a very nice service that you
could define as the "Google Docs" for developers. C9 offers you a
shared, always available on the cloud, environment to write your code.
They also offer access to a Linux terminal (so you can install
applications, like Django) and your websites are istantly available
online for remote testing.

[![c9ide\_django](http://www.andreagrandi.it/wp-content/uploads/2013/01/c9ide_django.png){.aligncenter
.wp-image-734 width="469"
height="345"}](http://www.andreagrandi.it/wp-content/uploads/2013/01/c9ide_django.png)

Installing and using Django on C9 is very easy. You just need to open a
new terminal tab (ALT+T) in C9 and execute these commands

\[sourcecode lang="text"\]  
easy\_install django  
python ./../bin/django-admin.py startproject myproject  
python ./myproject/manage.py runserver \$OPENSHIFT\_INTERNAL\_IP:\$PORT  
\[/sourcecode\]

After these commands, your Django website will be live and accessible
using **http://projectname.username.c9.io** (where *projectname* is the
name of the project you just created and *username* is your C9 user
name).

source: <http://support.cloud9ide.com/entries/21830983-django-development-in-c9>
