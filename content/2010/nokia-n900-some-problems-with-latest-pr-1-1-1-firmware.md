Title: Nokia N900: some problems with latest PR 1.1.1 firmware
Date: 2010-02-17 13:00
Author: admin
Category: Linux, Maemo (EN), Recensione
Tags: bug, firmware, maemo, N900, nokia
Slug: nokia-n900-some-problems-with-latest-pr-1-1-1-firmware
Status: published

I don't know if it's just a case or if I'm the only one who had these
problems, but I'll report them anyway, maybe somebody had my same
problem and we could try to prepare a proper bug report to make the
Maemo team fix them.

Infinite boot loop after upgrade
--------------------------------

First of all I have to say that before upgrading to PR 1.1.1 I checked
if I had enough space on the rootfs. I only had 27 Mb and so I decided
to remove some unused applications, deleted some \*.deb in
/var/cache/apt/archives and disabled extras repositories. Of course I
also did a backup of all my configuration. After the cleaning operation
I had near 60 Mb free on rootfs, enough to install the upgrade.

I closed all running applications, started the application manager and
began the upgrade. After the upgrade was completed, the device did a
reboot... then another one, then again, again.... until I had to remove
the battery to stop it.

Conclusion: I had to re-flash the device with the latest image to make
it work again.

mafw-dbus-wrapper taking all the CPU
------------------------------------

I was watching a video (using subtitles) and after some minutes the
whole UI became unresponsive. Strange because I already did this before
without having any problem. I tried to check the problem using "top"
utility from terminal and I saw that there was a mafw process
(mafw-dbus-wrapper) that was taking 80-90% of CPU. My fault is that
normally there are at least 3-4 , mafw-dbus-wrapper processes and I
didn't check which one was causing the problem. Anyway I made a
screenshot, just in case it can help.

[![](http://www.andreagrandi.it/wp-content/uploads/2010/02/Screenshot-20100217-034958-300x180.png "Screenshot-20100217-034958"){.size-medium
.wp-image-362 .aligncenter width="300"
height="180"}](http://www.andreagrandi.it/wp-content/uploads/2010/02/Screenshot-20100217-034958.png)

I hope this short report can be useful to help Maemo team to fix or at
least investigate what happened. Just leave a comment or contact me if
you need more informations.
