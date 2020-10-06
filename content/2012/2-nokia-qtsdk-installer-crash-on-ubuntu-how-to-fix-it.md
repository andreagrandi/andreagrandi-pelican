Title: Nokia QtSDK installer crash on Ubuntu: how to fix it
Date: 2012-01-12 19:36
Author: Andrea Grandi
Category: HowTo, Linux, Programmazione, Qt, Ubuntu (EN)
Tags: 11.04, 11.10, installer, Natty, nokia, Oneiric, Qt, SDK, Ubuntu
Slug: nokia-qtsdk-installer-crash-on-ubuntu-how-to-fix-it
Status: published

If you try to install **Nokia QtSDK** on Ubuntu using the Nokia
installer (that provides a newer version than the one distributed in
Ubuntu Software Center) you could get an error like this:

    :::shell
    (Qt_SDK_Lin32_offline_v1_1_3_en.run:3126): Gtk-CRITICAL **:
    IA__gtk_widget_style_get: assertion `GTK_IS_WIDGET (widget)`
    failed  

to fix it, you need to run the installer with a specific parameter:

    :::shell
    ./Qt_SDK_Lin32_offline_v1_1_4_en.run -style cleanlooks  

and everything should work!
