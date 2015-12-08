"""Default settings for the ``server_guardian_api`` app."""
from django.conf import settings


PROCESSORS = getattr(
    settings,
    'SERVER_GUARDIAN_PROCESSORS',
    []
)