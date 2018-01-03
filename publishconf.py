#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

# SITEURL = "//localhost/cuisine"
# XXX to build the site locally, comment this line
SITEURL = "//perso.crans.org/besson/cuisine"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_ANALYTICS = "UA-38514290-1"

GITHUB_URL = "https://github.com/Naereen/cuisine"
