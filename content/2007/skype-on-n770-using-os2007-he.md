Title: Skype on N770 (using Os2007 HE)
Date: 2007-12-10 15:00
Author: admin
Category: HowTo, Linux, Maemo (EN), Skype
Tags: 770, maemo, nokia, Skype
Slug: skype-on-n770-using-os2007-he
Status: published

Great news for all [N770]{style="font-weight: bold;"} users! Someone
discovered that is possible to make [Skype]{style="font-weight: bold;"}
run on N770 with [Os2007 HE]{style="font-weight: bold;"}.

All you have to do is follow these steps:

1\. Install skype-ui through Application Manager

2\. Download [this
package](http://catalogue.tableteer.nokia.com/certified/pool/chinook/user/s/skype/skype_1.7.62.48.5_armel.deb)
in your PC and extract the file named
[skyhost]{style="font-weight: bold;"}

3\. Find a way to copy the file **skyhost** to your maemo device in
**/usr/bin**

4\. execute this from root on your device:

`chown user:users /usr/bin/skyhost`

That's all! You can find more information on the [original
post](http://www.internettablettalk.com/forums/showthread.php?t=12740).
