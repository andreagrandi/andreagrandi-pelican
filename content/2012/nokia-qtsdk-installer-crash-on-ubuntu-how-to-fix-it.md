Title: Nokia QtSDK installer crash on Ubuntu: how to fix it
Date: 2012-01-12 19:36
Author: admin
Category: HowTo, Linux, Programmazione, Qt, Ubuntu (EN)
Tags: 11.04, 11.10, installer, Natty, nokia, Oneiric, Qt, SDK, Ubuntu
Slug: nokia-qtsdk-installer-crash-on-ubuntu-how-to-fix-it
Status: published

If you try to install **Nokia QtSDK** on Ubuntu using the Nokia
installer (that provides a newer version than the one distributed in
Ubuntu Software Center) you could get an error like this:

\[sourcecode lang="text"\]  
(Qt\_SDK\_Lin32\_offline\_v1\_1\_3\_en.run:3126): Gtk-CRITICAL \*\*:
IA\_\_gtk\_widget\_style\_get: assertion \`GTK\_IS\_WIDGET (widget)'
failed  
\[/sourcecode\]

to fix it, you need to run the installer with a specific parameter:

\[sourcecode lang="text"\]  
andrea@centurion:\~/Downloads/Qt\$
./Qt\_SDK\_Lin32\_offline\_v1\_1\_4\_en.run -style cleanlooks  
\[/sourcecode\]

and everything should work!
