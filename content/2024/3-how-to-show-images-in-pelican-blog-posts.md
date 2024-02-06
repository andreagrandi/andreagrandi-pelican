Title: How to show a cover image in Pelican based blog posts
Date: 2024-02-06 22:03
Author: Andrea Grandi
Category: Development
Tags: Pelican, Python, blog, writing, images, cover, template, open, graph, meta, social, media
Slug: how-to-show-cover-image-pelican-blog-posts
Status: published
Summary: How to add a cover image to Pelican based blog posts, so that when the article is shared on social media the image is shown in the preview.
Cover: images/2024/02/pelican-website-banner.jpeg

Once you have written and published an article, it’s very likely that you will want to **share** it on **social media** or send to your friends on a messaging app. 

One method to make the link more “attractive” is to include a **cover image** that will be shown in the link preview.

How do you set a cover image? You need to use a particular **Open Graph** tag named `og:image`.

[![A pelican with some code in the background ]({static}/images/2024/02/pelican-website-banner.jpeg)]()

## Open Graph

Open Graph is a [protocol](https://en.wikipedia.org/wiki/Facebook_Platform#Open_Graph_protocol) created by ~~Facebook~~ **Meta** to facilitate sharing articles and web pages on social media.

The syntax is very simple and all you have to do is to include a few meta tags in the header of your web page.

The most common tags to include are these ones:

- `og:title` is used as the main title of the page. It’s usually the biggest text being rendered 
- `og:description` is the additional text shown below the title
- `og:image` this is probably the most important tag to set, because it takes the biggest space wherever it’s being rendered 

## Pelican

Depending on the template you use, your Pelican based website may already support the `og:image` tag. 

For example in my case I need to add the `Cover` attribute to my page meta tags, like I did for this article:

```MarkDown
Title: How to show a cover image in Pelican based blog posts
Date: 2024-02-06 22:03
Author: Andrea Grandi
Category: Development
Tags: Pelican, Python, blog, writing, images, cover, template, open, graph, meta
Slug: how-to-show-cover-image-pelican-blog-posts
Status: published
Summary: How to add a cover image to Pelican based blog posts, so that when the article is shared on social media the image is shown in the preview.
Cover: images/2024/02/pelican-website-banner.jpeg
```

The template has a sub template (in my case it’s located [here](https://github.com/andreagrandi/andreagrandi.it/blob/master/themes/Flex/templates/partial/og_article.html)) may have something like this to render the image:

```jinja
{% if 'cover' in article.metadata %}
<meta property="og:image" content="{{ SITEURL }}/{{ article.metadata['cover'] }}">
{% else %}
<meta property="og:image" content="{{ SITELOGO }}">
{% endif %}
```

**Note:** if you don’t specify a Cover, the template will use your `SITELOGO` image.

If your template doesn’t have something like this, you may have to use one of the following **plugins**. For the specific instructions about how to use them, please refer to their readme on GitHub.

### pelican-seo plugin

[pelican-seo](https://github.com/pelican-plugins/seo) is a useful addition to your Pelican based website, even if your template already supports cover images, because it automatically adds all the Open Graph tags, which are useful to **boost the SEO** of your website.

### featured-image plugin

[featured-image](https://github.com/pelican-plugins/featured-image) is a much simpler plugin. All it does is to check if an image has already been included in the meta tags. If it’s not present, it tries to get the first one found in the page.

## Conclusion

Adding a cover image to your blog posts may seem a small thing, but it can make a huge difference if you decide to share your articles on social media.