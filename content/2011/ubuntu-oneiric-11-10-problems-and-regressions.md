Title: Ubuntu Oneiric 11.10 problems and regressions
Date: 2011-10-12 23:27
Author: admin
Category: Linux, Ubuntu (EN)
Tags: ubuntu oneiric ocelot
Slug: ubuntu-oneiric-11-10-problems-and-regressions
Status: published

<div>

![](http://www.andreagrandi.it/wp-content/uploads/2011/10/software-bug-300x199.jpg "software-bug-300x199"){.alignright
.size-full .wp-image-566 width="168" height="111"}

</div>

Tomorrow **Ubuntu 11.10** (Oneiric Ocelot) will be released officially
and I decided to test the RC (release candidate) version on my desktop
PC. Being involved in Unity-2D development I used only that desktop
environment on my development virtual machine so I didn't have much time
to test Unity (3D version).

I must admit that there have been a lot of improvements from 11.04
(Natty Narval) release, but also a lot of **bugs** and **regressions**
have been introduced. I've noted all the problems I found in every day
use and as soon as possible I'll also submit proper **bug report on
Launchpad** for each of them. In the mean time you can give a look to
the following list.

Bugs and regressions
--------------------

**Notifications broken:** on Ubuntu Natty when an application wants to
notify of a new message it popups an icon from the Launcher, then
displays a small blue triangle in the top-left corner of the screen.
Oneiric doesn’t have the small blue triangle anymore. In this way, if
the user is looking away when he gets a notification, he can miss it for
hours. There’s no way to know that there is a notify without manually
going with mouse to the left and making the launcher to appear.

**Launcher visibility:** on Ubuntu Natty when the user moves the mouse
in the top-left corner the Launcher is shown. Oneiric doesn’t show
Launcher if you move the mouse in the top-left corner. You can’t use the
top 30-40 pixels (the height of the panel).

**Notify area icons:** often in Oneiric when you click an icon in the
notify area (for example the volume icon, the network manager icon
ecc...) the popup is shown and suddenly hidden. You have to click a
second time to view it.

**Notify icon - Empathy:** in Oneiric you cannot open Empathy from the
notify area. If you click on “Chat” Empathy is open and visible on the
Launcher but not on the screen. You have to move to mouse to the
launcher then click on it to view the application window.

**Empathy:** “Automatically connect on startup” doesn’t work. If you
enable this option in Empathy it doesn’t start anyway when the system
start.

**Launcher doesn’t work as expected:** sometimes when you move the mouse
on the left, Launcher is not shown. You can try it many times and it
still doesn’t appear. I’ve to SUPER+D a couple of times (to show/hide
Desktop) to show view it. Even the opposite problem happens: sometime
you cannot hide the Launcher.

**Boot failing:** every time I boot Oneiric the first boot fails. I
cannot know what happens because nothing is shown on video. I press
CTRL+ALT+CANC, the system reboot and then boot normally.

**Showing Skype:** on Natty you just need to double-click on Skype icon
in the notify bar to show it, now you need to click once on the icon,
choose “Activate” from menu and you show it. Why the need to complicate
an easy thing?

**Webcam problems with Skype:** with Natty I could use my webcam with
Skype without any problem. Now I can still use it but if I activate the
view of myself during a videcall, the video completly locks and it
doesn’t work anymore. Skype is always the same version, so probably
there is a problem with the new driver used.

**Window manager:** sometimes moving an application window doesn’t work.
You drag a window around the screen then suddenly the window stop moving
and the mouse icon starts vibrating. You have to release and click again
to move the window and stop mouse icon vibrating.

[Conclusion]{.Apple-style-span style="font-size: 20px; font-weight: bold;"}
---------------------------------------------------------------------------

<div>

In the next days I'll work on checking for these bugs on Launchpad to
see if they're already submitted and if not I'll submit them, hoping
they will be fixed as soon as possible before end users start bothering
about them.

</div>
