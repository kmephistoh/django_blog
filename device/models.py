#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm

# Create your models here.

class DeviceRouter(models.Model):
	"""router info"""
	device_id = models.CharField(max_length=200)          #第几组
	mac = models.CharField(max_length=200, unique= True)
	state_info = models.CharField(max_length=200)
	extro_info = models.TextField()
	pub_date = models.DateTimeField('date_publisehd')

	def __unicode__(self):
		return self.device_id


class DeviceRouterForm(ModelForm):
    class Meta:
        model = DeviceRouter
        fields = ['device_id', 'mac', 'state_info', 'extro_info', 'pub_date']
        
	def __unicode__(self):
		return self.device_id
