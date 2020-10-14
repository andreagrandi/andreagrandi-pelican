Title: Improve your Pelican based website SEO by adding canonical url
Date: 2020-10-14 18:00
Author: Andrea Grandi
Category: Development
Tags: pelican, website, seo, canonical, url, optimisation, google, search
Slug: improve-pelican-based-website-seo-adding-canonical-url
Status: published
Summary: A quick trick to improve your Pelican based website SEO

You may have notice that a few days ago this website changed its template. I'm still using [Pelican](https://github.com/getpelican/pelican) static generator,
but I switched to a template named [Flex](https://github.com/alexandrevicenzi/Flex).

The template is really nice and it's also optimised for mobile clients, but it's not very optimised for SEO.

I'm in no way an expert, so I tried to research for ways to optimise Pelican based websites and I discovered something I didn't know.

## Content Duplication

If you are, like me, hosting your website on GitHub static pages, you should know that your published content is also duplicated on GitHub.
For example: the pages you see on <https://www.andreagrandi.it> are all available here <https://github.com/andreagrandi/andreagrandi.github.io>

This is a problem for search engines, because the content is the same, but they don't know which one is the website you would like to be found in the search results.

## Canonical URL

To solve this problem, pages needs to include a section like this:

    :::html
    <head>
        ...
        <link rel="canonical" href="https://www.andreagrandi.it/2020/10/11/python39-introduces-removeprefix-removesuffix/" />
    </head>

So even if that page is found [on GitHub](https://github.com/andreagrandi/andreagrandi.github.io/blob/master/2020/10/11/python39-introduces-removeprefix-removesuffix/index.html) Google will know that the "official" page is located at the `canonical` url and will use that url in the search results.

## How to fix your Pelican template

Adding the canonical url in Pelican based websites is quite simple. You need to add a section like this to your `base.html` template file:

    :::html
        ...
        {% if article %}
            <link rel="canonical" href="{{ SITEURL }}/{{ article.url }}" />
        {% endif%}
    </head>

At this point, just rebuild and publish your pages and you are done!

## References

- <https://blog.kmonsoor.com/pelican-how-to-make-seo-friendly/>
- <https://moz.com/learn/seo/canonicalization>
