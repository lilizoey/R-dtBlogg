#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rødt Østensjø'
SITENAME = 'Rødt Østensjø'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Oslo'

DEFAULT_LANG = 'no'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_DATE = (1970, 1, 1, 0, 0, 0)


THEME = "/home/sayaks/pelican-themes/foundation-default-colours"
PLUGINS = ["plugins.foundation_images"]

# Theme settings

FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Drevet av <a href="http://getpelican.com">Pelican</a> og <a href="http://foundation.zurb.com/">Zurb Foundation</a>. Theme fra <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
FOUNDATION_PYGMENT_THEME = 'monokai'

# Blogroll
LINKS = (('Rødt', 'https://roedt.no/'),
         ('Bli Medlem', 'https://roedt.no/innmelding/'),
         ('Avisa Rødt Nytt', 'https://roedt.no/rodt-nytt'),
         ('Rødt oslo', 'https://roedt.no/oslo/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

LOCALE = ('nb_NO', 'no')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True