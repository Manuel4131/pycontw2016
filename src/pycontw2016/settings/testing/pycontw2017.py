import os

from .base import STATICFILES_DIRS, TEMPLATES
from .base import *     # noqa


CONFERENCE_DEFAULT_SLUG = 'pycontw-2017'
TEMPLATES[0]['DIRS'][0] = os.path.join(
    TEMPLATES[0]['DIRS'][0], CONFERENCE_DEFAULT_SLUG,
)
STATICFILES_DIRS[0] = os.path.join(
    STATICFILES_DIRS[0], CONFERENCE_DEFAULT_SLUG,
)

EVENTS_PUBLISHED = False
