
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nabin Bhattarai'
SITENAME = 'Nabin Bhattarai'
BIO_TEXT = 'Programmer, AI Researcher.'

TWITTER_USERNAME = '@nabin_xinzus'

# SITEURL = 'https://nbnhattarai.github.io'
SITEURL = 'http://localhost:8000'

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/files/resume.pdf" target="_blank">Resume</a>',
    '<a href="/archive/">Archive</a>',
]

ICONS_PATH = 'images/icons'

SOCIAL_ICONS = [
    ('mailto:nbn.bhattarai99@gmail.com',
     'Email (nbn.bhattarai99@gmail.com)', 'fa-envelope'),
    ('http://twitter.com/nabin_xinzus', 'Twitter', 'fa-twitter'),
    ('http://github.com/nbnbhattarai', 'GitHub', 'fa-github'),
    # ('/atom.xml', 'Atom Feed', 'fa-rss'),
]

THEME_COLOR = '#FF8000'

TIMEZONE = 'Asia/Kathmandu'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

PATH = 'content'
ARTICLE_PATHS = ['blog', ]
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

TYPOGRIFY = True

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

THEME = 'themes/pneumatic'

PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['assets', 'neighbors', 'render_math']

TIPUE_SEARCH = True

TEMPLATES = ['404.html']
TEMPLATE_PAGES = {page: page for page in TEMPLATES}

STATIC_PATHS = ['images', 'uploads', 'extra', 'files']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

EXTRAS = ['CNAME', 'favicon.ico', 'keybase.txt', 'robots.txt']
EXTRA_PATH_METADATA = {'extra{}'.format(
    _file): {'path': _file} for _file in EXTRAS}

ASSET_SOURCE_PATHS = ['static']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'linenums': None}
    }
}

ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]
