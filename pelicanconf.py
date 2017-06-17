#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lilian Besson'
SITENAME = 'Recettes de cuisine - Lilian Besson'
SITEURL = ''
# SITEURL = 'http://perso.crans.org/besson/cuisine'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Mon site', 'http://perso.crans.org/besson/'),
    ('Pelican', 'http://GetPelican.com/'),
    ('Python', 'https://Python.org/'),
    ('Marmiton', 'http://marmiton.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://GitHub.com/Naereen'),
    ('bitbucket', 'https://Bitbucket.org/lbesson'),
    ('facebook', 'https://www.Facebook.com/naereencorp.lbesson'),
)

DEFAULT_PAGINATION = 10

DEFAULT_DATE = 'fs'

DEFAULT_CATEGORY = 'recette'

STATIC_PATHS = [
    'images',
    # 'pdfs'
]

FAVICON = 'favicon.ico'

SIDEBAR_DIGEST = 'Recettes classiques et expériences en cuisine'

TYPOGRIFY = True

# SLUGIFY_SOURCE = 'title'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = 'notmyidea'
# THEME = 'blue-penguin'
THEME = 'pelican-blue'

# css_file = "wide.css"
