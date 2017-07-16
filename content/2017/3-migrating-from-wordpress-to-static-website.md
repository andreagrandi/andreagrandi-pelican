Title: Migrating from WordPress to a static generated website
Date: 2017-07-02 13:00
Author: Andrea Grandi
Category: Development
Tags: Python, Pelican, static, website, migration, CloudFlare, GitHub
Slug: migrating-from-wordpress-to-static-generated-website
Status: published

As you may have noticed, my website looks very different compared to a few days ago.
It's just a different theme or template, I completely changed how the pages are generated and
I'm hosting it in a completely different way.

### A brief history

When I started this blog 10 years ago, I was hosting it on a shared hosting service and it was based on **WordPress**.
I then decided to keep WordPress as backend (I don't like PHP very much but I wasn't even good at front end development at the time,
so using a tool that allowed me to concentrate on the content rather than on design was a natural choice for me) but to move my website
to a **VPS** on **DigitalOcean**, where I've self-hosted **Nginx + PHP + MySQL** and even Postfix for email aliases until a few days ago.

### Why moving to a static website?

In these three or four years I've been using a VPS, I must say I've been good enough (or maybe lucky?) at keeping "bad people" out
of my server, but it's true that **maintaining a VPS can be very time consuming** and you can never be sure that your website is always safe.
I've heard about static website before, but I was a bit skeptic because I had not spent enough time investigating all the possibilities
(search and comments are still possible, thanks to external services and plugins).

Another advantage of a static website is that I can perfectly "run" (preview) on my local computer without publishing it online. Pages can be rendered locally
and will appear in the browser exactly as they will appear once published online.

If you use a tool like WordPress, you need to be constantly connected to Internet to write any change. With static pages **I can write my content offline**
(so I can do it while commuting on the train or while I'm flying somewhere) and publish it once I'm back online.

### Pelican

The tool that I'm using to generate this website is called [Pelican](https://blog.getpelican.com/). 
There are many [static website generators](https://www.staticgen.com/), the reason why I chose Pelican is because it's written in **Python**,
so if I need to do any change I can do them and because its templates use Jinja2 which I'm already familiar with. It can also import posts from WordPress
(and I had over 180 posts to import from my previous website) so if you are migrating from it it's a good choice. Please note that the import script is not perfect
and that you may have to adjust some formatting here and there.

### A new deployment pipeline

When you use WordPress your website is already online and all you have to do is to login, use the integrated editor, write content and finally publish it.
A static website doesn't have any admin tool, it's just static pages. How do you publish content then? There are of course multiple solutions available.
In my case my website source code is hosted in [a repository on GitHub](https://github.com/andreagrandi/andreagrandi.it). When I commit on **master** branch
there is a webhook that triggers a [build job](https://github.com/andreagrandi/andreagrandi.it/blob/master/.travis.yml) on [TravisCI](https://travis-ci.org/).
TravisCI fetches the latest source code, installs Pelican on the CI and builds the static pages. Once the build is finished, a [bash script](https://github.com/andreagrandi/andreagrandi.it/blob/master/deploy.sh) is used to **publish**
the generated pages on the static website hosting service.

### Hosting a static website

The good thing about hosting a static website is that you don't need a database so you can host it almost anywhere at a cheaper price or even for free.
In my case I've decided to use **GitHub pages**, mainly for simplicity. Every GitHub user can have a static website hosted at <yourusername\>.github.io for free.
To start using it, you just have to create a repository named <yourusername\>.github.io under your GitHub account. In my case the repository is [https://github.com/andreagrandi/andreagrandi.github.io](https://github.com/andreagrandi/andreagrandi.github.io). My deploy script simply takes the generated content
that is in the output/ folder and **git push** it on this repository. Once the website has been pushed to git, it's immediately available at **https://andreagrandi.github.io**

#### CloudFlare

GitHub Pages service has a little limitation: you can either have your website served from a URL similar to the one I've just mentioned, including SSL support *or* you can use your own domain, but **you can't have both things** (SSL + custom domain). To workaround this, you can instruct your domain registrar (in my case is [Gandi.net](https://www.gandi.net/)) to let CloudFlare manage your domain and just enabling "Full SSL" support will do the trick. I won't repeat here how to use CloudFlare since they have a very nice tutorial explaining how to configure their service to be used with GitHub Pages: [https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/](https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/). Remember to include a **CNAME** file containing your domain name and let your static generetor put it on the root of your website, otherwise GitHub pages won't serve the pages correctly.

#### Why not Amazon S3?

While I was looking for instructions about how to host a static websites, I found many examples of websites using Amazon S3. There is nothing wrong with using this service (just keep in mind that it's not free, Amazon charges you for space usage and requests, so keep an eye on the AWS bill) but the way these websites were using it was completely wrong. The most common error I noticed was the fact they were enabling the **flexible SSL** option on CloudFlare: this means that the connection between the visitor and CloudFlare was encrypted (and visitor could see the the SSL enabled) but the connection between CloudFlare and Amazon S3 was being served with **HTTP only**, meaning that potentially the pages could have been modified before being served. Infact Amazon doesn't serve the S3 website buckets with SSL, they use plain HTTP (Why are you doing this Amazon?!). To use the S3 bucket correctly one should also configure Route 53 (to manage DNS) and CloudFront (the Amazon equivalent of CloudFlare service, beware because this is also charged separately depending on usage/traffic), making the whole setup a bit more complicated.

### Conclusion

I finally moved away from my VPS and from now on I will be able to concentrate my time on content only instead of spending part of it to maintain my server. Last but not least, the possibility to write my content offline, will hopefully allow me to write from places (train, airplane) where I've never written from before. If you have any suggestion or if if you notice any error, feel free to leave a comment here below. In alternative, since now this blog is completely open source and on GitHub, you can fork it and make a pull request!
