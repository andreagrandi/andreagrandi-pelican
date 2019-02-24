Title: How to deploy a static website to Github Pages using CircleCI
Date: 2019-02-24 11:00
Author: Andrea Grandi
Category: Web
Tags: ci, circleci, github, static, website, deploy
Slug: how-to-deploy-static-website-github-pages-circleci
Status: draft

Since I created my blog with a static pages generator, I've been using TravisCI to automate the pages build and deployment.
My desire to learn something new (we are using CircleCI at work, but I never configured it from scratch) and the recent news about
TravisCI [acquisition](https://blog.travis-ci.com/2019-01-23-travis-ci-joins-idera-inc) and employees [layoff](https://twitter.com/alicegoldfuss/status/1098604563664420865), led me to think about moving to a different service.

## Github Pages

Every account on Github can use a special repository to publish static pages. In my case, since I have `github.com/andreagrandi`, my special repository is
named `github.com/andreagrandi.github.io`. Once I publish my pages there, they will be accessible from `https://andreagrandi.github.io`.

You will need to use the **master** branch of the special repository directly and not the **gh-pages** branch which is available to each repository.

## CircleCI

CircleCI is a very flexible and powerful continuous integration tool, which is also **free** for open source projects. As long as your static website is located on a public repository on Github, you won't have to pay anything to use it. In my case, the surce code of this website is available at [https://github.com/andreagrandi/andreagrandi.it](https://github.com/andreagrandi/andreagrandi.it)


### Configuration

You can find the complete configuration at [this address](https://github.com/andreagrandi/andreagrandi.it/blob/master/.circleci/config.yml).
The only value you won't find is **GH_TOKEN**. You need to generate this token on Github, at this address: [https://github.com/settings/tokens](https://github.com/settings/tokens). Give it a nice description like "CircleCI deployment token", select **repo** scope and finally click **Generate token** button. This token will be used to `git push...`
your pages once they are built. Please remember to keep this token **secret** and not to publish it anywhere.

In my configuration you may notice that I'm using [Pelican](https://blog.getpelican.com/) static websites generator, but apart from a few changes, the structure of the configuration should be very similar even if you use Jekill, Hugo etc... it doesn't really matter how you generate the pages, the **deployment phase will be the same**.

### Deployment script

You will notice that there is a complete bash script embedded in the CircleCI configuration. This script configures git, fetches the existing `andreagrandi.github.io` repository,
and sync the built pages with the existing ones (this avoid creating a commit which contains all the pages so it will contain just the added content). Once the commit is made, the script will finally push the changes to the repository.

**Please note:** regardless of CircleCI settings, the deployment will only happens if we are pushing (or merging a pull request) to **master** (`if [ "${CIRCLE_BRANCH}" = "master" ]; then`) and it will actually commit and push pages only if there is something new to commit (`if git commit -m "CircleCI build $CIRCLE_BUILD_NUM pushed to Github Pages" ; then`). For example if I'm just updating something in the CircleCI configuration, which doesn't change anything in the content, the pages won't be deployed again.

## Conclusion

My first impression of CircleCI is that is faster than TravisCI and this means that I can publish my content more quickly. The possibility of using Docker containers as base image is really powerful and in more complex scenarios we can reproduce the building environment locally on our machine. If you have any advices about how to improve my build script, feel free to leave a comment here.
