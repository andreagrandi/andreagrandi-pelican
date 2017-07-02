Title: Installing qemu-arm-eabi patch into Scratchbox
Date: 2007-11-16 15:49
Author: admin
Category: HowTo, Linux, Maemo (EN), Programmazione
Tags: maemo, qemu, scratchbox, SDK
Slug: installing-qemu-arm-eabi-patch-into-scratchbox
Status: published

Using Scratchbox and in particular the Maemo SDK with ARMEL target, very
often when we try to execute some application we can get into this kind
of errors (for example):

`sem_post: Function not implemented`

This happens because not all the functions have been implemented in the
emulated environment.[ Lauro Venâncio]{style="font-weight: bold;"} has
created a [patched](http://sourceforge.net/projects/qemu-arm-eabi/)
version of qemu-arm called [qemu-arm-eabi]{style="font-weight: bold;"}.

Thanks to [Marcelo Lira]{style="font-weight: bold;"}, we have a simple
howto to install the patch into the Scratchbox environment.
[Note:]{style="font-weight: bold;"} you have to execute these commands
from outside the Scratchbox environment and you should not be logged
into the environment at the same time.

[1.]{style="font-weight: bold;"} You need gcc 3.4, SDL dev library and
Zlib dev:[  
]{style="font-size: 78%;"}

`sudo apt-get install gcc-3.4 libsdl1.2-dev zlib1g-dev`

[2.]{style="font-weight: bold;"} Get the patched qemu-arm. Notice that
the patches are already applied, everything is here, and you don't need
to get the qemu sources.

` svn co  https://qemu-arm-eabi.svn.sourceforge.net/svnroot/qemu-arm-eabi qemu-arm-eabi cd qemu-arm-eabi ./configure --target-list=arm-linux-user --static make`

[3.]{style="font-weight: bold;"} Copy qemu to the cputransp dir on
scratchbox[  
]{style="font-size: 78%;"}

`sudo cp arm-linux-user/qemu-arm /scratchbox/devkits/cputransp/bin/qemu-arm-eabi-sb2`

[4.]{style="font-weight: bold;"} Add it to the list of cputransp
methods. Open the file[  
]{style="font-size: 78%;"}

`sudo vim /scratchbox/devkits/cputransp/etc/cputransp-methods`

and add this line:

`qemu-arm-eabi-sb2`

[5.]{style="font-weight: bold;"} Configure the target to use the patched
qemu as transparency method. Edit the file:[  
]{style="font-size: 78%; font-family: courier new;"}

`vim /scratchbox/users/USERNAME/targets/CHINOOK_ARMEL.config`

and change this line:

`SBOX_CPUTRANSPARENCY_METHOD=/scratchbox/devkits/cputransp/bin/qemu-arm-eabi-sb2`

That's all! You're now ready to log again into your Scratchbox
environment.
