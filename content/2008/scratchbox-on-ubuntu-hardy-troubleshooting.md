Title: Scratchbox on Ubuntu Hardy troubleshooting
Date: 2008-04-21 14:37
Author: admin
Category: Maemo (EN)
Tags: maemo, nokia, scratchbox, SDK, tablet
Slug: scratchbox-on-ubuntu-hardy-troubleshooting
Status: published

Yesterday I **upgraded** from **Ubuntu 7.10** to the new **8.04 RC** and
I "broke" my Scratchbox installation. I tried to install it again and I
had still some problems logging into **Scratchbox** and installing the
**SDK**.

The I found this page:
<http://suppressingfire.livejournal.com/35277.html>

that explain how to fix these problems. In particular if you get this
kind of error trying to log into Scratchbox:

`` Inconsistency detected by ld.so: rtld.c: 1192: dl_main: Assertion `(void *) ph->p_vaddr == _rtld_local._dl_sysinfo_dso' failed! ``

You can fix it in this way:

`echo 0 | sudo tee /proc/sys/vm/vdso_enabled`

You can read the complete fix in my updated wiki:
<http://www.ptlug.org/wiki/Howto_Installing_Maemo_SDK_4>
