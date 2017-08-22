# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Tu botella se ha guardado en la caba correctamente")
		return render(request, "home.html", {}) # HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"title": "Wine Cellar",
		"obj_list": queryset
	}
	return render(request, "home.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Your <a href='#'>Bottle</a> is modificated.", extra_tags="html_safe")
		return render(request, "home.html", {}) # HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id)
	instance.delete()
	messages.success(request, "Your <a href='#'>Bottle</a> is deleted.")
	return redirect("posts:list")