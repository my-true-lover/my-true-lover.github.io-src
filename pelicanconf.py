#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristin'
SITENAME = "Kristin's Stuff"
SITESUBTITLE = 'All the stuff that Kristin likes'
SITEURL = 'https://my-true-lover.github.io'

THEME = './theme'
PLUGIN_PATHS = ['/home/us11334/.pelican/plugins']
PLUGINS = ['photos']

PHOTO_LIBRARY = '~/repos/kblog_pelly/photos'
PHOTO_GALLERY = (2048, 1536, 100)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/index.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = 'rss/index.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Pujangga', 'https://github.com/habibillah/pujangga'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/RistinEigh'),
          ('Github', 'https://github.com/my-true-lover'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']

ARTICLE_URL = 'posts/{slug}/'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'

TWITTER_USERNAME = 'RistinEigh'
