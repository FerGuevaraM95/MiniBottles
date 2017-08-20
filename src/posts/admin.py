# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "update", "timestamp"]
	list_display_links = ["title"]
	list_filter = ["timestamp"]
	search_fields = ["title", "description"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)