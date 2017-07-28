# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

from blog.models import Post


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.name, self.email, self.url, self.text, self.create_time, self.post)