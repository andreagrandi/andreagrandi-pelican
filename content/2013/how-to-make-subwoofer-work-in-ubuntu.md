Title: How to make subwoofer work in Ubuntu
Date: 2013-06-22 19:19
Author: admin
Category: HowTo, Linux, Ubuntu (EN)
Tags: sound, subwoofer, Ubuntu
Slug: how-to-make-subwoofer-work-in-ubuntu
Status: published

Using the same computer with Windows 8 and Ubuntu I noticed that the
sound was worse in Ubuntu and I discovered why soon: **subwoofer**
doesn't work out of the box!

How to fix it
-------------

The fix is quite easy to apply (but it was not easy to find the right
one!). First of all edit **/etc/pulse/default.pa** and add this line at
the end:

    load-module module-combine channels=6 channel_map=front-left,front-right,rear-left,rear-right,front-center,lfe

then edit **/etc/pulse/daemon.conf**, modify the line
"enable-lfe-remixing: no" to "**enable-lfe-remixing: yes**", then
uncomment it (remove the semicolon in front of it). Reboot your PC and
enjoy the subwoofer!

References
----------

-   <http://forums.gentoo.org/viewtopic-t-859769.html>
-   <http://askubuntu.com/questions/53802/subwoofer-sound-preferences-problem>

