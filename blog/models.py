# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import timezone

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章阅读量
    views = models.PositiveIntegerField(default=0)
    # article title
    title = models.CharField(max_length=100)
    # article create time
    create_time = models.DateTimeField('date article create')
    # article modified time
    # modified_time = models.DateTimeField()
    # article excerpt 可以为空值
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    #  正文
    body = models.TextField(blank=True)
    # 文章标签 一篇文章可以有多个标签 一个标签也可以用于多个标签
    tag = models.ManyToManyField(Tag, blank=True)
    # 作者
    user = models.ForeignKey(User)

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 保存文章阅读量
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 文章评论数量
    def comment_counts(self):
        return self.comment_set.count()

    def __str__(self):
        return '%s %s %s %s' % (self.title, self.tag, self.create_time, self.user)