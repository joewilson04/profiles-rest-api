# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
