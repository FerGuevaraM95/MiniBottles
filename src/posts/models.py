# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings 
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to=upload_location,
		null=False, 
		blank=False,
		height_field="height_field",
		width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	category = models.CharField(max_length=50)
	origin = models.CharField(max_length=50)
	ml = models.IntegerField(default=0)
	description = models.TextField(max_length=256)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})		

	class Meta:
		ordering = ["-timestamp", "-update"]	