Title: Moving away from Google Talk to a real Jabber/XMPP service
Date: 2015-02-20 21:15
Author: admin
Category: HowTo, Linux
Tags: chat, Google, gtalk, im, jabber, xmpp
Slug: moving-away-from-google-talk-to-a-real-jabberxmpp-service
Status: published

I've been recently concerned about [the
future](https://plus.google.com/+MayurKamat/posts/ETBvtp9VYav) of
**Google Talk** service and all the implications related to recent
changes to the existing service. What has been a nice implementation of
the [Jabber/XMPP](http://en.wikipedia.org/wiki/XMPP) protocol once, now
is just a [closed and
proprietary](https://www.eff.org/deeplinks/2013/05/google-abandons-open-standards-instant-messaging)
service. The main problem with these changes are:

-   Jabber/XMPP users of other services won't be able to talk anymore to
    Google Talk users
-   Google is killing some of their native clients (like the Windows
    one) and forcing users to Chrome or Android/iOS versions
-   Google has disabled the possibility to turn off chat recording (you
    can still do it individually, for each contact)

So, what are the alternatives to Google Talk? Luckly you have at least
three options.

Using an existing Jabber/XMPP service
-------------------------------------

This is surely the easiest way to get a Jabber/XMPP account. There is a
list of free services available
here: <https://xmpp.net/directory.php> registering a new account is
usually very easy. Most of the clients have an option that let you
register the account while you are configuring it. For example if you
are using [**Pidgin**](https://www.pidgin.im) and you want to register
an account with
[DukGo](https://duck.co/blog/using-pidgin-with-xmpp-jabber) service, you
can configure it in this way:

[![2\_addaccount](http://www.andreagrandi.it/wp-content/uploads/2015/02/2_addaccount.png){.aligncenter
.size-full .wp-image-928 width="348"
height="531"}](http://www.andreagrandi.it/wp-content/uploads/2015/02/2_addaccount.png)

 

Using an hosted Jabber/XMPP service with your domain
----------------------------------------------------

A service called [**HostedIM**](http://hosted.im) offer a very nice
service. Basically if you already have a domain, you can register an
account on [hosted.im](http://hosted.im), setup your **DNS** following
their instructions and create an account directly on their dashboard.
You can create up to **5 accounts for free**. If you need more, they
offer a paid service for that. In my case all I had to do was updating
my DNS with the following configuration:

    _xmpp-client._tcp.andreagrandi.it. IN SRV 10 0 5222 xmpp1.hosted.im.
    _xmpp-client._tcp.andreagrandi.it. IN SRV 20 0 5222 xmpp2.hosted.im.
    _xmpp-server._tcp.andreagrandi.it. IN SRV 20 0 5269 xmpp2.hosted.im.
    _xmpp-server._tcp.andreagrandi.it. IN SRV 10 0 5269 xmpp1.hosted.im.
    _jabber._tcp.andreagrandi.it. IN SRV 20 0 5269 xmpp2.hosted.im.
    _jabber._tcp.andreagrandi.it. IN SRV 10 0 5269 xmpp1.hosted.im.

Hosting your own Jabber/XMPP service
------------------------------------

If you have a VPS and some syasdmin skills, why not hosting your own
XMPP server? There are different options available, but I can suggest
you three in particular:

-   [OpenFire](http://www.igniterealtime.org/projects/openfire/)
-   [ejabberd](https://www.ejabberd.im/)
-   [Prosody](http://prosody.im/)

I haven't tried any of these personally, because for the moment I'm
using the service offered by hosted.im. I'm curious anyway to configure
at least one of them and when I will do it I will publish a dedicated
tutorial about it.

Conclusion
----------

Given the recent changes that Google is doing to all their services, I'm
more than happy when I can abandon one of them, because I personally
don't like to rely (and bind myself) to a single company, expecially if
that company closes a service whenever they want and try to lock you
inside their ecosystem.
