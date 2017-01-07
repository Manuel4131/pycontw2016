import os

from ..local import STATICFILES_DIRS, TEMPLATES
from ..local import *   # noqa

DEBUG = False

LANGUAGE_CODE = 'en-us'

CONFERENCE_DEFAULT_SLUG = 'testing'
TEMPLATES[0]['DIRS'][0] = os.path.join(
    TEMPLATES[0]['DIRS'][0], CONFERENCE_DEFAULT_SLUG,
)
STATICFILES_DIRS[0] = os.path.join(
    STATICFILES_DIRS[0], CONFERENCE_DEFAULT_SLUG,
)

EVENTS_PUBLISHED = True
