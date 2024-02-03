Title: Blogging from an iPad
Date: 2024-02-1 17:00
Author: Andrea Grandi
Category: Writing
Tags: development, tutorial, howto, writing, iOS, shortcuts, MWeb, git
Slug: blogging-from-an-ipad
Status: draft
Summary: In this post I share my findings and my current setup which allows me to write and publish blog posts from my iPad, for my static generated blog, powered by Pelican and GitHub Pages.

A few years ago, I [migrated](https://www.andreagrandi.it/2017/07/02/migrating-from-wordpress-to-static-generated-website/) from my Wordpress based blog (which I self hosted… yeah… I know… no comment!) to a static generated (using [Pelican](https://getpelican.com/)) one which is hosted (for free!) on GitHub Pages.

This setup, believe me or not, is cool. I’ve all my blog posts written in **MarkDown**, versioned on and kept safe on GitHub and when I’m ready to publish, I just need to make a pull request, merge it and a CI job will take care of using Pelican to build the pages and push them to the right place. You can find more information about my setup in [this other post](https://www.andreagrandi.it/2019/02/24/how-to-deploy-static-website-github-pages-circleci/).

So, what’s the problem? Well, as you can imagine, to do all of this, you need a GitHub client, a MarkDown editor and you need to be able to commit, push and do pull requests.

Is this  possible from an iPad? I believed it wasn’t (since the official GitHub client is very limited on what you can do, and online IDEs like VsCode.dev requires an internet connection, and I would like to be able to write also when I’m offline), but thanks to this [blog post](https://www.marcogomiero.com/posts/2021/running-blog-ipad/) from **Marco Gomiero**, I recently found out it’s possible!

[![Frankenstein Junior - It could work!]({static}/images/2024/02/it-could-work.jpeg)]()

## Working Copy: git client for iOS

The most important part of my workflow would not be possible without this amazing git client.

[![Working Copy]({static}/images/2024/02/working-copy.jpeg)]()

[Working Copy](https://workingcopy.app/) is so far the best Git client you can find on iOS. It allows you to clone repositories and work offline. Checked out content is made available through the File explorer, so any iOS app has access to it and this means you can use any client to edit your files.

## MWeb: a simple MarkDown editor for iOS

Following the suggestion from Marco’s blog post I decided to start using [this editor](https://www.mweb.im/index.html). To be honest I’m still not sold on it (literally: I haven’t purchased it yet and I’m still using the free version), because I’ve found a couple of issues which I’ve promptly reported to the author (let’s see if and how long it will take for them to reply) but they are not bad enough to entirely disrupt my workflow.

In case MWeb should not work for me, I’m planning to try a few others: [Textastic](https://www.textasticapp.com/), [iWriter Pro](https://serpensoft.info/index.html) and maybe [iA Writer](https://ia.net/writer) (but for its cost it has to be damn perfect!)

[![MWeb]({static}/images/2024/02/editing-markdown-with-mweb.jpeg)]()

## iOS Shortcuts and Automations

Another idea I borrowed from Marco is the usage of **iOS Shortcuts**.

In my case I had to customise the flow quite a lot, either because I use Pelican instead of Hugo, and also because I’ve some conventions I want to follow when writing my blog posts, but overall I implemented similar features:

- “New Blog Post”: the first shortcut creates a new branch in my repository and creates a new MarkDown file, following my own convention. Then it fills the empty file with some headers which are normally used in Pelican MarkDown files.
- “Blog Photo”: this shortcut let me select a photo from my gallery, it converts it to JPEG (most of the time pictures taken with my iPhone had *.heic format, so they need to be converted) and place it in the expected folder in my repository.

## Conclusion

Thanks for reading my first blog post, entirely written from my iPad, while I was relaxing on my sofa. If you have any questions or suggestions for a good MarkDown editor for iOS, feel free to leave a comment.
