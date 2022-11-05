#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.andreagrandi.it'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'andrea-grandi-it'
TAG_FEED_RSS = 'feeds/{slug}.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
GOOGLE_ANALYTICS = 'UA-2140684-3'
