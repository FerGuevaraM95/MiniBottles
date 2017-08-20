# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.
def post_create(request):
	return HttpResponse("<h1>Crear</h1>")

def post_detail(request):
	instance = get_object_or_404(Post, id=3)
	context = {
		"title": instance.titulo,
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

def post_update(request):
	return HttpResponse("<h1>Modificar</h1>")

def post_delete(request):
	return HttpResponse("<h1>Eliminar</h1>")