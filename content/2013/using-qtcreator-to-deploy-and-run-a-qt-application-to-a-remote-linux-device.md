Title: Using QtCreator to deploy and run a Qt application to a remote Linux device
Date: 2013-01-17 18:49
Author: admin
Category: HowTo, Linux, Programmazione, Qt, Ubuntu (EN)
Tags: deploy, Linux, Qt, QtCreator, SDK, Ubuntu
Slug: using-qtcreator-to-deploy-and-run-a-qt-application-to-a-remote-linux-device
Status: published

QtCreator is a very flexible IDE and can really be adapted for a lot of
things. I usually use it to develop mobile applications for Nokia N9 and
BlackBerry 10, but it can be used for more generic tasks. In my case I
wanted to be able to develop a Qt application using my desktop PC,
deploy it and run on a remote (actually it's on the same desk) Linux
machine running Xubuntu.

Doing this is quite easy and you don't need any specific plugin on
QtCreator, but be sure to have at least version 2.6.x. Other than
QtCreator you also need two Linux based PC (I used Ubuntu 12.10 for my
development machine and Xubuntu 12.10 for the remote netbook) and an SSH
account on the remote PC.

Add the remote device to QtCreator {#add-the-remote-device-to-qtcreator style="text-align: left;"}
----------------------------------

![QtCreatorDevice](http://www.andreagrandi.it/wp-content/uploads/2013/01/QtCreatorDevice.png){.aligncenter
.wp-image-748 width="488" height="282"}

To add the remote Linux device on QtCreator, use the
**Tools-&gt;Options** menu and click on "**Devices**" item. At this
point click on "**Add**" button and fill the fields using values similar
to the screenshot. In particular specify a **name** for the device, the
**IP** of the remote machine and a **username** and **password** that
must already exist (I just created the user "andrea" on the Xubuntu
machine and used the same password). I also had to set the **timeout**
to 20 seconds, because I had some connection problems and the connection
kept dropping after 10 seconds trying. To verify if everything is
working fine, just click on **Test** button.

Add a specific Qt version
-------------------------

[![QtCreatorQtVersion](http://www.andreagrandi.it/wp-content/uploads/2013/01/QtCreatorQtVersion.png){.aligncenter
.size-full .wp-image-754 width="488"
height="282"}](http://www.andreagrandi.it/wp-content/uploads/2013/01/QtCreatorQtVersion.png)

To write your application you may need a specific Qt version that is
different from the one distributed by your Linux distribution. There's
no problem, QtCreator let you add different Qt versions without any
conflict. In my case I installed the Qt5 version distributed by
**Canonical Qt5 Edgers
Team**: <https://launchpad.net/~canonical-qt5-edgers>  
Once it's installed, just click on "**Add**" button and select the qmake
specific to the version you want to add (in my case it was in
**/opt/qt5/bin/qmake** ).

Add a Qt Kit
------------

[![QtCreatorQtKits](http://www.andreagrandi.it/wp-content/uploads/2013/01/QtCreatorQtKits.png){.aligncenter
.size-full .wp-image-757 width="488"
height="282"}](http://www.andreagrandi.it/wp-content/uploads/2013/01/QtCreatorQtKits.png)

QtCreator permits to add new **Kit** (development configurations) and
these kits are used during project creation to specify what you want to
target. In my example I added a new kit choosing an appropriate **name**
"Qt5 Ubuntu", the **device type**, the actual **device** previously
configured and finally the **Qt version** that we added before. With a
kit I have a complete "toolchain" that allow me to write applications
for a particular device, with a specific Qt version.

Putting the pieces together
---------------------------

At this point you just have to create a new "**Qt Quick 2**"
application, and select the new kit you just created instead of the
"Desktop" one. **Please note** that there is a little problem that I
haven't fixed yet (but I'm working on it): if you create, for example, a
project named "QtTest1" it will be deployed to the folder /opt/QtTest1/
on the remote machine. By default your user doesn't have read+write
permissions for that folder so I manualy created the folder and I gave a
chmod 777 on it, just for testing. There are two possible ways to fix
this: you could create a specific user that has read+write permissions
on /opt/ or you could modify the deployment configuration to have the
app deployed to the user /home (I will investigate on this possibility
and I will write something in one of the next posts).

Final thoughts
--------------

What all of this could be useful for? Well, do 2+2 and you'll easily
guess ;) In the next weeks I will post more specific informations and I
will update everyone with my progresses. Any comment is welcome! If you
want to contribute to this you're welcome too of course.
