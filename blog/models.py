#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm

# Create your models here.

class Article(models.Model):
	"""blog Article"""
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField('date_publisehd')
	likes = models.IntegerField()

	def __unicode__(self):
		return self.title


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'pub_date', 'likes']
        
	def __unicode__(self):
		return self.title

