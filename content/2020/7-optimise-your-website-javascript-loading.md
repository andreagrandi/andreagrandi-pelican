Title: Optimise your website JavaScript loading speed with defer
Date: 2020-10-15 20:00
Author: Andrea Grandi
Category: Development
Tags: optimisation, optimise, javascript, js, website, web, performance, speed, defer, page, fast, loading, webpage, quicker
Slug: optimise-website-javascript-loading-speed
Status: published
Summary: A simple way to optimise the websites loading speed by deferring javascript download

When a client requests a web page, the browser begins to download the html page and parses it. If an external resource is found
it begins to request that resource in a parallel request. This means the the complete **loading of the page may be delayed until all the external resources have been downloaded**. On mobile or slow connections, this can be a problem.

[![speed road]({static}/images/2020/10/speed_road.jpg){ width=60% }]()

## The solution

While it's not possible to fix all the external resources, there is an attribute called `defer` that when included in `<script> ... </script>` sections, it will make sure that javascript files will be loaded **after** the main page has been loaded, resulting in a quicker download of the main content.

### Example

If you have a script like this:

    :::html
    <script src="https://www.andreagrandi.it/theme/tipuesearch/tipuesearch.min.js" type="5ea4254e9004c2f036fc9ad2-text/javascript"></script>

just add the `defer` attribute like this:

    :::html
    <script defer src="https://www.andreagrandi.it/theme/tipuesearch/tipuesearch.min.js" type="5ea4254e9004c2f036fc9ad2-text/javascript"></script>

## Compatibility

Even if the `defer` option should be supported by the majority of the browsers, it's always better to double check which are the browsers not supporting it yet.
You can check the compatibility at this address: <https://caniuse.com/script-defer>

**Note:** the `defer` attribute can't always be used in all the pages. When you need a script to be available before the page is completely rendered, you can't use it. You may have noticed that in this website I haven't deferred the loading of `jquery` library. For example, I don't know all the details, but I suppose it's necessary to load, parse and render the search results for Tipue Search. Infact if I defer the script, no search results will appear in my website.

## References

- <https://flaviocopes.com/javascript-async-defer/#just-tell-me-the-best-way>
