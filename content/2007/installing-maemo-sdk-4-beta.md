Title: Installing Maemo SDK 4 Beta
Date: 2007-10-25 16:24
Author: admin
Category: HowTo, Linux, Maemo (EN), Programmazione
Tags: maemo, nokia, SDK, tablet
Slug: installing-maemo-sdk-4-beta
Status: published

Introduction
------------

**Maemo** is an opensource development platform for **Linux** based
devices. Actually is the base for the operating system installed on
**Nokia**
[N770](http://www.nokia.it/770 "http://www.nokia.it/770"){.external
.text},
[N800](http://europe.nokia.com/phones/n800 "http://europe.nokia.com/phones/n800"){.external
.text} and the upcoming
[N810](http://www.nokia.com/N810 "http://www.nokia.com/N810"){.external
.text} but it could be adopted, with few changes, even by other similar
devices.

In particular, this version of Maemo SDK is the only one that allow
developers to develop new applications for **N810** and to start porting
old application to this new platform.

The SDK is not only a set of libraries and compiler, it gives you a real
environment that emulates the Nokia device, so the developer can write
applications, debug them and test them. Both command line and gui
application are supported in emulator.

Graphical environment is based on a real **X server**, a **window
manager** and on **GTK** libraries, with a particular extension called
**Hildon**.

With Maemo SDK you can:

-   Test Maemo applications using a normal PC with Linux.
-   Write and debug applications written by you.
-   Port existing applications written for Linux/GTK and verify if they
    work correctly.
-   Compile and build ARMEL package so you can install them in the
    device.

[]{#Requirements}

Requirements
------------

These are the minimum requirements to work with Maemo SDK:

-   Intel compatible processor (x86), at least 500 Mhz
-   256 Mb RAM
-   2 Gb space on hard disk
-   A Linux distribution (I suggest Debian or Ubuntu)

You need the following software packages:

-   Scratchbox: a cross-compiling toolkit that allows you to compile
    applications for different platform
-   Maemo SDK: you can find it at this address:
    <http://www.maemo.org/downloads/download-sdk.html>
-   Xephyr Xserver:

Starting from **4.x** version, Maemo has a simple installer script, so
all you need are these two files:

-   [maemo-scratchbox-install\_4.0beta.sh](http://tabletsdev.maemo.org/unstable/chinook-beta/maemo-scratchbox-install_4.0beta.sh "http://tabletsdev.maemo.org/unstable/chinook-beta/maemo-scratchbox-install_4.0beta.sh"){.external
    .text}
-   [maemo-sdk-install\_4.0beta.sh](http://tabletsdev.maemo.org/unstable/chinook-beta/maemo-sdk-install_4.0beta.sh "http://tabletsdev.maemo.org/unstable/chinook-beta/maemo-sdk-install_4.0beta.sh"){.external
    .text}

[]{#Installing_Scratchbox}

Installing Scratchbox
---------------------

The first tool you have to install is **Scratchbox**. I suggest you to
use the script provided but you could choose also to install it manually
(in this case please refer to \[[this
site](http://scratchbox.org/documentation/user/scratchbox-1.0/html/installdoc.html "http://scratchbox.org/documentation/user/scratchbox-1.0/html/installdoc.html"){.external
.text}\] for detailed instructions).

Before beginning the installation of Scratchbox, you have to become
**root**.

First of all set the permission of the script file:

`chmod +x maemo-scratchbox-install_4.0beta.sh`

Then run it with these parameters:

`./maemo-scratchbox-install_4.0beta.sh -d -u andy80`

Please note that **-d** tells the installer to install from Debian dpkg
packages while **-u** specifies your username (in my case is andy80, you
have to change it using your local username).

Scratchbox environment will be installed in /scratchbox/

Please note that you'll have to logout and login again to be able to log
into you new Scratchbox environment. To test it you simply have to start
Scratchbox from your local user:  
` andy80@noteboontu:~/download/maemo_4.0_beta$ /scratchbox/login`

Welcome to Scratchbox, the cross-compilation toolkit!

Use 'sb-menu' to change your compilation target.  
See /scratchbox/doc/ for documentation.

\[sbox-SDK\_BETA\_ARMEL: \~\]  
</code>

[]{#Installing_Maemo_SDK}

Installing Maemo SDK
--------------------

When Scratchbox is correctly installed on your system, you can install
the **Maemo SDK**. Please note that you have to do it from **normal
user** (the user you specified in the installation of Scratchbox).

Simply run this command and follow instructions:

`bash maemo-sdk-install_4.0beta.sh`

At the end you should get this message:

` Installation was successful! ----------------------------`

IMPORTANT! Please read this.

You now have the maemo 4.0beta 'chinook' installed on your computer.  
You can now start your maemo SDK session with /scratchbox/login and  
then select your target with 'sb-conf select SDK\_BETA\_ARMEL' for the  
armel target or 'sb-conf select SDK\_BETA\_X86' for the i386 target.

If you have any problems with targets' package databases, you can try  
running 'fakeroot apt-get -f install' on your scratchbox target.  
This command will try to fix any problems with the package database.

Happy hacking!  
</code>

[]{#Installing_Xephyr}

Installing Xephyr
-----------------

Xephyr is an X11 server that provides a device screen for the developer
so that you can see all the maemo application windows and visuals on
your computer.

To install it in a Debian based distribution, simply execute this (from
root):

` apt-get install xserver-xephyr`

[]{#Running_Xephyr}

Running Xephyr
--------------

To see if all works fine, you should start Xephyr and Maemo environment.
Execute this from outside the Scratchbox environment:

`Xephyr :2 -host-cursor -screen 800x480x16 -dpi 96 -ac -extension Composite`

Now, from another shell, log into Scratchbox and execute this:  
` [sbox-SDK_BETA_X86:~] > export DISPLAY=:2 [sbox-SDK_BETA_X86:~] > af-sb-init.sh start`

This should start the Hildon Application Framework inside the Xephyr
window. That's all!

[]{#References}

References
----------

Here you can find a list of website where I took information from to
write this guide:

-   <http://tabletsdev.maemo.org/unstable/chinook-beta/INSTALL.txt>
-   [http://www.maemo.org](http://www.maemo.org/ "http://www.maemo.org"){.external
    .free}

