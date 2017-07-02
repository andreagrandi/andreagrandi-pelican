Title: Using Twitter Bootstrap with Node.js, Express and Jade
Date: 2013-02-24 21:05
Author: admin
Category: HowTo, Linux, Node.js, Programmazione, Ubuntu (EN)
Tags: Bootstrap, css, Express, Jade, Javascript, NodeJs, npm, twitter, Ubuntu
Slug: using-twitter-bootstrap-with-node-js-express-and-jade
Status: published

I've decided to write this post as a note to myself. I'm still learning
Node.js and digging into Express/Jade, but I've read many people using
the nice [**Twitter Bootstrap**](http://twitter.github.com/bootstrap/)
and I was wondering if there was a way to integrate all these
technologies. The short answer is: yes, we can!

**Note:** once again, I'm not a Node.js expert and surely there are
other ways to achieve this task (for example there is a Node.js module
called
[**twitter-bootstrap**](https://npmjs.org/package/twitter-bootstrap),
but I haven't tried it). This tutorial is based on another tutorial I
found, but it was not very updated and it had a more complicated way to
install Bootstrap, so I decided to write a new one basing it on the
original <http://www.rs.au.com/31/how-to-install-bootstrap-v2-0-2-in-expressjs-v3-0-0>

Preparing the environment
-------------------------

I will assume that you're running any Linux distribution (in my case I'm
using Ubuntu 12.10, but feel free to use your own distribution). Be sure
to have installed a recent version of **nodejs** and **npm** packages
(I'm using Node.js 0.8.20 and npm 1.2.11).

### Create a project folder and install the required dependencies

    mkdir node-bootstrap
    cd node-bootstrap
    npm install express
    npm install jade

Create the basic project structure with Express
-----------------------------------------------

    andrea@andrea-Inspiron-660:~/Documents/sviluppo/nodejs/node-bootstrap$ node_modules/express/bin/express nodebootstrap

    create : nodebootstrap
    create : nodebootstrap/package.json
    create : nodebootstrap/app.js
    create : nodebootstrap/public
    create : nodebootstrap/public/javascripts
    create : nodebootstrap/public/images
    create : nodebootstrap/public/stylesheets
    create : nodebootstrap/public/stylesheets/style.css
    create : nodebootstrap/routes
    create : nodebootstrap/routes/index.js
    create : nodebootstrap/routes/user.js
    create : nodebootstrap/views
    create : nodebootstrap/views/layout.jade
    create : nodebootstrap/views/index.jade

    install dependencies:
    $ cd nodebootstrap && npm install

    run the app:
    $ node app

You should already have installed all the needed dependencies, even
without executing **npm install**, anyway executing it won't hurt.

Download and install Bootstrap
------------------------------

Download Twitter Boostrap from the official
website <http://twitter.github.com/bootstrap/assets/bootstrap.zip> and
unzip it under the **nodebootstrap/public** folder.

Bootstrap integration with Jade template system
-----------------------------------------------

At this point you need to edit the **views/layout.jade** file and
include the references to Bootsrap

    !!!
    html
      head
        title= title
        link(rel='stylesheet', href='/bootstrap/css/bootstrap.min.css')
        link(rel='stylesheet', href='/bootstrap/css/bootstrap-responsive.min.css')
        link(rel='stylesheet', href='/stylesheets/style.css')
        script(src='https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js')
        script(src='/bootstrap/js/bootstrap.min.js')
      body
        block content

Test the Bootstrap integration

At this point we will modify **views/index.jade** that is the default
template used to render the index

extends layout

    block content
      div.top
        form.form-horizontal(method="post", id="loginForm")
          label Username
          input.span3(id="username", type="text", name="User", placeholder="Enter your username")
          label Password
          input.span3(id="password", type="password", name="Password")
          input.btn(type="submit", value="Log In")
      div.container
        div.content
          table.table.table-striped
            thead
              tr
                th Table
                th Heading
            tbody
              tr
                td Blah
                td Test
              tr
                td Hello
                td World

      div.footer

Now go back to the terminal and execute the app:

    andrea@andrea-Inspiron-660:~/Documents/sviluppo/nodejs/node-bootstrap/nodebootstrap$ node app.js
    Express server listening on port 3000

Open your favourite browse and visit <http://localhost:3000> to see your
first Bootstrap + Node.js application app and running.
