Title: wxGTK working on Maemo
Date: 2007-12-17 14:48
Author: Andrea Grandi
Category: HowTo, Linux, Maemo (EN), Programmazione
Tags: maemo, SDK, tablet, wx
Slug: wxgtk-working-on-maemo
Status: published

Reading the [official WxWidget blog](http://wxwidgets.blogspot.com/2007/11/hildonizing-wxgtk.html), I
discovered that one of their developer was working to hildonize
[WxWidgets]{style="font-weight: bold;"}. I wanted to know if that was
just a test or if this library could work in Maemo, so I followed his
suggestion and I grabbed the latest SVN sources:

    :::shell
    svn checkout http://svn.wxwidgets.org/svn/wx/wxWidgets/trunk wxWidgets

and I compiled it in this way:

    :::shell
    cd wxWidgets ./configure --with-hildon make make install

then I grabbed a simple "HelloWorld" from the official documentation.
You can find the complete source code [here](http://www.wxwidgets.org/docs/tutorials/hworld.txt).

I compiled the source code in this way:

    :::shell
    g++ hworld.cpp wx-config --libs wx-config --cxxflags -o hworld

then I ran it in the usual way:

    :::shell
    run-standalone.sh ./hworld

The result? I think that a screenshoot is better than thousand words :)

[![](http://bp0.blogger.com/_eBt7-uNFVjs/R2QhZl8EwLI/AAAAAAAAAJ0/rdNTRYsp_n8/s400/wxWindowsHildon.jpg)](http://bp0.blogger.com/_eBt7-uNFVjs/R2QhZl8EwLI/AAAAAAAAAJ0/rdNTRYsp_n8/s1600-h/wxWindowsHildon.jpg)

**Note:** I tested this inside Scratchbox,
using **CHINOOK_x86** target, so I think it will work fine on Os2008. This could be a good thing to help other
developers porting some interesting applications (uhm... aMule for example ;) ) to Maemo.
