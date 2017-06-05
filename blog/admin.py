# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Categorie, Article

admin.site.register(Categorie)
admin.site.register(Article)
