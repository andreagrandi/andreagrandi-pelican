Title: Why I completely switched this website to HTTPS (and why you should do the same)
Date: 2015-08-22 14:59
Author: admin
Category: Sicurezza
Slug: why-i-completely-switched-this-website-to-https-and-why-you-should-do-the-same
Status: published

I must admit it, there was a time when I was not using **HTTPS**, not
even to protect the admin section of the website. This means that anyone
could have intercepted the password and published (or deleted) things in
my name. Since a couple of years ago I started protecting my admin
sectio using an SSL certificate.  I haven't done it before for a couple
of reason: my hosting was on a provider that required a lot of money
(something like 100\$/year) to enable SSL support, plus an SSL
certificated costed at least 100-120\$/year.

When I migrated my website on my own [VPS on
DigitalOcean](https://www.digitalocean.com/?refcode=cc8349e328a5) I
finally discovered that **[StartSSL](https://www.startssl.com)** was
giving **free class 1 certificates** and I immediately got one. I made
the mistake to just serve the admin pages using HTTPS, not all the
website. I regretted about this decision after readin a
[couple](http://dannyman.toldme.com/2010/12/23/swa-yahoo-being-evil/) of
[articles](http://opensource.com/business/15/8/interview-daniel-roesler-utilityapi)
that were explaining how some internet providers where changing served
HTTP pages injecting their own ads or banner. That was unacceptable to
me and I swicthed the whole website to HTTPS.

Basically, if you don't serve even your personal website using HTTPS,
someone could change the page while it's being transfered to the
requester. Imagine if you have (like me) a page on your blog that let
people download your public PGP key. Users could be served with a
different key, so someone else would be able to decrypt a message
intended for you only. Scary, isn't it?

If you need more informations about how to request a StartSSL
certificate and how to install it on Nginx/Apache, I can suggest this
nice tutorial: <https://konklone.com/post/switch-to-https-now-for-free>

If you need to serve a WordPress website, that configuration is not
enough. In that case you may want to have a look at my own Nginx
configuration, available at this
address: <https://gist.github.com/andreagrandi/5de9dc9c4eb7e732764c>

p.s: if you are you curious to try how Digital Ocean VPS works and fancy
**10\$ credit** (enough for 2 months if you choose the basic droplet)
for **free, u**se this link and enjoy
it <https://www.digitalocean.com/?refcode=cc8349e328a5>
