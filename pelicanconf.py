import logging
from datetime import datetime

LOG_FILTER = [(logging.INFO, 'Empty alt attribute for image %s in %s')]

AUTHOR = 'Bhavin Tandel'
SITENAME = 'Professional Portfolio'
SITEURL = ''

THEME = 'Flex'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Menu settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False


ARTICLE_URL = '{category}/{slug}/{date:%Y}/{date:%m}/'
ARTICLE_SAVE_AS = '{category}/{slug}/{date:%Y}/{date:%m}/index.html'

# Static paths
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Projects settings
ARTICLE_PATHS = ['blogs']
PAGE_PATHS = ['pages']

# CATEGORY_URL = 'category/{slug}/'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Add the following lines to include the blog index page
MENUITEMS = [
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
]

IGNORE_FILES = [
    '.#*',
    '__pycache__',
    '.pytest_cache'
]

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/bhavintandel/'),
    ('Github', 'https://github.com/bhavintandel'),
    )

DEFAULT_PAGINATION = 10

# Sitemap settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'pages': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'monthly',
        'indexes': 'daily',
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

COPYRIGHT_YEAR = datetime.now().year

USE_LESS = True
DEFAULT_PAGINATION = 20