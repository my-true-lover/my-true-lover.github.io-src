#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristin'
SITENAME = 'Psalm 63 Housewife'
SITESUBTITLE = 'My lips will glorify You because Your faithful love is better than life'
SITEURL = ''

THEME = './theme'
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['gallery',
           'image_process',]

GALLERY_PATH = './photos'

IMAGE_PROCESS = {
    'thumb' : {'type' : 'image',
               'ops' : ['scale_in 200 200 True'],
               }
                 }

#PHOTO_LIBRARY = '~/repos/kblog_pelly/photos'
#PHOTO_GALLERY = (2048, 1536, 100)
#PHOTO_ARTICLE = (760, 506, 80)
#PHOTO_THUMB = (192, 144, 60)

PATH = './content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/RistinEigh'),
          ('Github', 'https://github.com/my-true-lover'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['photos',]

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'

TWITTER_USERNAME = 'RistinEigh'
