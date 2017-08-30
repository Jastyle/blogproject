# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Tag, Category, MyAuthor

# Register your models here.


admin.site.register(Tag)
admin.site.register(Category)


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'email']
#     search_fields = ['first_name', 'email']

admin.site.register(MyAuthor)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'create_time']
#     search_fields = ['create_time']
#     fields = ['title', 'tag']
admin.site.register(Post)