# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	nombre = models.CharField(max_length=50)
	imagen = models.FileField(null=False, blank=True)
	descripcion = models.TextField(max_length=256)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.nombre