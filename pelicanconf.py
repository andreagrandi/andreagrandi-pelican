#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os


AUTHOR = u'Andrea Grandi'
SITENAME = u'Andrea Grandi'
SITEURL = os.environ.get('SITEURL', 'http://localhost:8000')

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/andreagrandi'),
    ('github', 'https://github.com/andreagrandi'),
    ('linkedin', 'https://www.linkedin.com/in/andreagrandi/'),
)

DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DISPLAY_CATEGORIES_ON_MENU = False
STATIC_PATHS = [
    'images', 'extra/CNAME', 'extra/favicon.ico', 'extra/keybase.txt',
    'extra/2240402E.asc']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
    'extra/2240402E.asc': {'path': '2240402E.asc'},
}

THEME = 'themes/Flex'
PLUGIN_PATHS = ['plugins']

from pelican_jupyter import markup as nb_markup
PLUGINS = ['tipue_search', nb_markup]
IGNORE_FILES = [".ipynb_checkpoints"]

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
DISPLAY_SEARCH_FORM = True
DISPLAY_CATEGORIES_ON_POSTINFO = True
MARKUP = ('md', 'ipynb')

MAIN_MENU = True
SITETITLE = "Andrea Grandi"
SITESUBTITLE = "Software Developer"
SITELOGO = "/images/me_pycon_2019_2_300x300.jpg"
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
COPYRIGHT_YEAR = datetime.now().year

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}
DISABLE_URL_HASH = True
