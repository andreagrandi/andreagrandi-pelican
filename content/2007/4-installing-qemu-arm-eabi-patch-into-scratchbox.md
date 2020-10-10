Title: Installing qemu-arm-eabi patch into Scratchbox
Date: 2007-11-16 15:49
Author: Andrea Grandi
Category: HowTo, Linux, Maemo (EN), Programmazione
Tags: maemo, qemu, scratchbox, SDK
Slug: installing-qemu-arm-eabi-patch-into-scratchbox
Status: published

Using Scratchbox and in particular the Maemo SDK with ARMEL target, very
often when we try to execute some application we can get into this kind
of errors (for example):

    :::shell
    sem_post: Function not implemented

This happens because not all the functions have been implemented in the
emulated environment.[ Lauro Venâncio]{style="font-weight: bold;"} has
created a [patched](http://sourceforge.net/projects/qemu-arm-eabi/)
version of qemu-arm called [qemu-arm-eabi].

Thanks to **Marcelo Lira**, we have a simple
howto to install the patch into the Scratchbox environment.

**Note:** you have to execute these commands
from outside the Scratchbox environment and you should not be logged
into the environment at the same time.

You need gcc 3.4, SDL dev library andZlib dev:

    :::shell
    sudo apt-get install gcc-3.4 libsdl1.2-dev zlib1g-dev

Get the patched qemu-arm. Notice that
the patches are already applied, everything is here, and you don't need
to get the qemu sources.

    :::shell
    svn co https://qemu-arm-eabi.svn.sourceforge.net/svnroot/qemu-arm-eabi qemu-arm-eabi 
    cd qemu-arm-eabi 
    ./configure --target-list=arm-linux-user --static make

Copy qemu to the cputransp dir on scratchbox:

    :::shell
    sudo cp arm-linux-user/qemu-arm /scratchbox/devkits/cputransp/bin/qemu-arm-eabi-sb2

Add it to the list of cputransp methods. Open the file:

    :::shell
    sudo vim /scratchbox/devkits/cputransp/etc/cputransp-methods

and add this line:

    :::bash
    qemu-arm-eabi-sb2

Configure the target to use the patched qemu as transparency method. Edit the file:

    :::shell
    vim /scratchbox/users/USERNAME/targets/CHINOOK_ARMEL.config

and change this line:

    :::shell
    SBOX_CPUTRANSPARENCY_METHOD=/scratchbox/devkits/cputransp/bin/qemu-arm-eabi-sb2

That's all! You're now ready to log again into your Scratchbox
environment.
