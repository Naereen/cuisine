#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Recettes de cuisine - par Lilian Besson"
AUTHOR = "Lilian Besson"
SITEURL = ""
# SITEURL = "http://perso.crans.org/besson/cuisine"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Sources (GitHub)", "https://GitHub.com/Naereen/cuisine"),
    ("Mon site",         "http://perso.crans.org/besson/"),
    ("Pelican",          "http://GetPelican.com/"),
    ("Python.org",       "https://Python.org/"),
    # ("Marmiton.org",     "http://marmiton.org/"),
)

MENU_LINKS = (
    ("Sources (GitHub)", "https://GitHub.com/Naereen/cuisine"),
    ("Mon site",         "http://perso.crans.org/besson/"),
)

# Social widget
SOCIAL = (
    ("github",       "https://GitHub.com/Naereen"),
    ("bitbucket",    "https://Bitbucket.org/lbesson"),
    ("facebook",     "https://www.Facebook.com/naereencorp.lbesson"),
    ("address-card", "http://perso.crans.org/besson/callme.html"),
    ("wikipedia-w",  "https://fr.wikipedia.org/wiki/User:Naereen"),
    ("envelope",     "mailto:naereen at crans dot org"),
    ("phone",        "tel:+33 6 28 41 22 57"),
    ("rss",          "http://perso.crans.org/besson/cuisine/feeds/all.atom.xml"),
)
ICONS = SOCIAL

DEFAULT_PAGINATION = 10

DEFAULT_DATE = "fs"

DEFAULT_CATEGORY = "recette"

STATIC_PATHS = [
    "images",
    # "pdfs"
]

FAVICON = "images/favicon.ico"

LOGOPATH = "images/icon.png"
SITEIMAGE = LOGO = LOGOPATH

DESCRIPTION = "Des recettes classiques \U0001F378 et des expériences en cuisine \u2728 !"
WELCOME_MESSAGE = SIDEBAR_DIGEST = SITESUBTITLE = DESCRIPTION

TYPOGRIFY = True

# SLUGIFY_SOURCE = "title"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "notmyidea"
THEME = "themes/alchemy"

# css_file = "wide.css"

PLUGIN_PATHS = [
    "plugins/pelican-plugins"
]

PLUGINS = [
    # https://github.com/getpelican/pelican-plugins/tree/master/assets
    # "assets",
    # https://github.com/getpelican/pelican-plugins/tree/master/global_license
    "global_license",
    # https://github.com/getpelican/pelican-plugins/tree/master/neighbors
    "neighbors",
    # https://github.com/kura/pelican-githubprojects/
    # "pelican-githubprojects",
    # https://github.com/getpelican/pelican-plugins/tree/master/random_article
    "random_article",
    # https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
    # "tag_cloud",
]

LICENSE = "MIT License"

GITHUB_USER = "naereen"

TEMPLATE_PAGES = {
    'templates/github-projects.html':
        'pages/github-projects.html',
}

RANDOM = 'random.html'

PYGMENTS_STYLE = 'monokai'
