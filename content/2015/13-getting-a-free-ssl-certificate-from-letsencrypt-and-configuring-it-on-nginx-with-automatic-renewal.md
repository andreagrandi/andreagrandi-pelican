Title: Getting a free SSL certificate from Letsencrypt and configuring it on Nginx with automatic renewal
Date: 2015-12-06 14:15
Author: admin
Category: DevOps, HowTo, Linux
Tags: encryption, letsencrypt, security, ssl
Slug: getting-a-free-ssl-certificate-from-letsencrypt-and-configuring-it-on-nginx-with-automatic-renewal
Status: published

Finally **[Letsencrypt](https://letsencrypt.org/)** went to **public
beta** and I really couldn't wait to use it on my VPS (where this blog
is hosted). Until few days ago I was using a **free SSL** certificate
from [StartSSL](https://www.startssl.com/). The service is nice and I'm
grateful to them for this important resource they are providing for
free, but it must be said that their renewal procedure isn't one of the
most user friendly.

For people who don't know the service yet, **Letsencrypt** not only
gives **free SSL certificates**, they also provide a command line tool
that people can use to request a new certificate or to renew an existing
one. This means that you don't have to worry anymore if/when your
certificate expires, you can set a crontab command and have the
certificate **automatically renewed** for you.

Client installation
-------------------

To request a SSL certificate you need to install their command line
utility. Unless it has already been packaged for your distribution, for
the moment it's much easier to get it from git as they explain in their
[installation
instructions](https://letsencrypt.readthedocs.org/en/latest/using.html#installation):

``` {.lang:sh .decode:true}
git clone https://github.com/letsencrypt/letsencrypt
cd letsencrypt
./letsencrypt-auto
```

Getting the SSL certificate
---------------------------

There are a few different options available to request a certificate,
but the easiest one is to use the **--webroot** option, specifying the
document root of your website so that the client will be able to put
there a verification (temporary) file that will be served to the remote
service and used as verification method. In my case I only needed this
command:

``` {.lang:sh .decode:true}
./letsencrypt-auto certonly --webroot -w /var/www/andreagrandi.it/ -d www.andreagrandi.it -d andreagrandi.it --email myemail@myprovider.com --renew-by-default --agree-tos
```

Please note that I had to specify both www.andreagrandi.it and
andreagrandi.it as domains, otherwise it would have been invalid when
requesting just andreagrandi.it resources.

Configuration files and certificates installation
-------------------------------------------------

The command above will save all the configuration under
**/etc/letsencrypt/** and all the generated certificates under
**/etc/letsencrypt/live/www.andreagrandi.it/\*.pem** (all the \*.pem
files here are symbolic links to the current certificate). If you are
using **Nginx** the only files you need are **fullchain.pem** and
**privkey.pem** and you can set them in your Nginx configuration using
these two parameters:

``` {.lang:default .decode:true}
ssl_certificate /etc/letsencrypt/live/www.andreagrandi.it/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/www.andreagrandi.it/privkey.pem;
```

In case you want to have a look at my full Nginx configuration file, as
reference, you can find it
here <https://gist.github.com/andreagrandi/8b194c99cd3e77fdb5a8>

Automatic renewal
-----------------

The last thing to be configured is a crontab rule to call the script
every... 2 months. Why 2 months? Letsencrypt SSL **certificates expire
in 3 months**. Usually SSL certificates are valid at least for 1 year,
but Letsencrypt decided to make it 3 months to incentivate the
automation of the renewal. I set it to 2 months, so if anything goes
wrong I still have plenty of time to do it manually. To edit crontab for
root user execute **crontab -e** and add this line:

``` {.lang:default .decode:true}
0 3 1 */2 * /root/letsencrypt/letsencrypt-auto certonly --webroot -w /var/www/andreagrandi.it/ -d www.andreagrandi.it -d andreagrandi.it --email email@domain.com --renew-by-default --agree-tos && service nginx reload
```

Just a final note. You may have noticed that this website presents an
SSL certificate issued by COMODO. That's because I have
**[CloudFlare](https://www.cloudflare.com/)** in front of my website and
that's how their SSL strict option works (at least for free plans).

 
