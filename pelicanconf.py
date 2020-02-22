#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import shutil
import logging

AUTHOR = 'Nabin Bhattarai'
SITENAME = 'Nabin Bhattarai'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL_ICONS = [
    ('mailto:nbn.bhattarai99@gmail.com',
     'Email (nbn.bhattarai99@gmail.com)', 'fa-envelope'),
    ('http://twitter.com/nabin_xinzus', 'Twitter', 'fa-twitter'),
    ('http://github.com/nbnbhattarai', 'GitHub', 'fa-github'),
]

DEFAULT_PAGINATION = 10

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['']

ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
DRAFT_URL = 'blog/{slug}/'
DRAFT_SAVE_AS = 'blog/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/{slug}/'
CATEGORY_SAVE_AS = 'blog/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

AUTHORS_SAVE_AS = None  # Not used
CATEGORIES_SAVE_AS = None  # Not used
TAGS_SAVE_AS = None  # Not used

STATIC_URL = 'static/{path}'
STATIC_SAVE_AS = 'static/{path}'
STATIC_PATHS = ['img', 'files']
EXTRA_PATH_METADATA = {'img/favicon.ico': {'path': '../favicon.ico'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.abbr',
           'm.alias',
           'm.code',
           'm.components',
           'm.dot',
           'm.dox',
           'm.filesize',
           'm.gh',
           'm.gl',
           'm.htmlsanity',
           'm.images',
           'm.link',
           'm.math',
           'm.metadata',
           'm.plots',
           'm.sphinx',
           'm.vk']

FORMATTED_FIELDS = ['summary', 'description',
                    'landing', 'badge', 'header', 'footer']

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
# DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css', '/static/css/custom.css']

M_THEME_COLOR = '#22272e'

# M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
#                '/static/m-light.css', '/static/css/custom.css']
# M_THEME_COLOR = '#cb4b16'

M_IMAGES_REQUIRE_ALT_TEXT = True
M_METADATA_AUTHOR_PATH = 'blog/authors'
M_METADATA_CATEGORY_PATH = 'blog/categories'
M_METADATA_TAG_PATH = 'blog/tags'

if not shutil.which('latex'):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True

DIRECT_TEMPLATES = ['archives']
PAGINATED_TEMPLATES = {'archives': None,
                       'tag': None, 'category': None, 'author': None}

M_BLOG_NAME = 'Nabin Bhattarai'
M_BLOG_URL = 'blog/'
M_FAVICON = ('favicon.ico', 'image/x-ico')

ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['blog/authors', 'blog/categories', 'blog/tags']

# M_SITE_LOGO = 'logo.png'
M_SITE_LOGO_TEXT = 'Nabin Bhattarai'

M_LINKS_NAVBAR2 = [
    # ('About', 'about/', 'about', []),
    ('Blog', 'blog/', '[blog]', []),
    # ('Contact', 'contact/', 'contact', []),
]

M_FINE_PRINT = SITENAME + \
    """. Powered by `Pelican <https://getpelican.com>`_ and `m.css <https://mcss.mosra.cz>`_."""

M_FINE_PRINT = """
Copyright © `Nabin Bhattarai <mailto:nbn.bhattarai99@gmail.com>`_, 2019. All rights
reserved.
""" + """
Powered by `Pelican <https://getpelican.com>`_ and `m.css <https://mcss.mosra.cz>`_."""

M_FINE_PRINT = ''

PUBLICATIONS_SRC = 'content/pubs.bib'
