# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Player,Player_lite

admin.site.register(Player)
admin.site.register(Player_lite)
