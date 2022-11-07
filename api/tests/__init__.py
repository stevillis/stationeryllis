"""Test related config."""

import os

from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stationeryllis.settings")
setup()
