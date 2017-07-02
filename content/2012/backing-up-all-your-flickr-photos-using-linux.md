Title: Backing up all your Flickr photos using Linux
Date: 2012-01-05 11:31
Author: admin
Category: HowTo, Linux, Python, Ubuntu (EN)
Slug: backing-up-all-your-flickr-photos-using-linux
Status: published

I've been a Flickr pro user for 4 years, but the pro account costs
**24,95\$/year** and I was looking for something cheaper. Anyway I was
thinking that after all, even if I don't renew my account, I can always
access to all my pictures.... wrong! **If you don't renew your pro
Flickr account you can only access to the low resolution version of your
own pictures.** That's not acceptable for me, so I decided to download
all my pictures and upload them somewhere else. Here comes the second
disappointment: **there is no automatic way to download all your
pictures**.

I simply had no time to write an application by myself, so I started
searching on Google to see if there was something available to do this
simple task. At the beginning I only found abandoned tools (closed
source, the API was expired ecc...), paid tools, Windows only tools
ecc... but finally I found this
post <http://hivelogic.com/articles/backing-up-flickr/>

There is a Python script that automatically downloads all your Flickr
pictures getting the highest resolution available, you can download the
script from here <https://github.com/dan/hivelogic-flickrtouchr>

The usage is very simple

\[sourcecode lang="text"\]  
mkdir FlickrBackupFolder  
python flickrtouchr.py FlickrBackupFolder  
\[/sourcecode\]

A browser's window will be opened and you'll be prompted for
authorization. After that, all you pictures will be downloaded.
