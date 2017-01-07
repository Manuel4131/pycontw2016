import os

from .base import STATICFILES_DIRS, TEMPLATES
from .base import *     # noqa

# Override static and media URL for prefix in WSGI server.
# https://code.djangoproject.com/ticket/25598
STATIC_URL = '/2016/static/'
MEDIA_URL = '/2016/media/'

CONFERENCE_DEFAULT_SLUG = 'pycontw-2016'
TEMPLATES[0]['DIRS'][0] = os.path.join(
    TEMPLATES[0]['DIRS'][0], CONFERENCE_DEFAULT_SLUG,
)
STATICFILES_DIRS[0] = os.path.join(
    STATICFILES_DIRS[0], CONFERENCE_DEFAULT_SLUG,
)
