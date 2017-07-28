# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Tag, Category
# Register your models here.


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)