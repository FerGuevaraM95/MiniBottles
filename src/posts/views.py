# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def post_create(request):
	return HttpResponse("<h1>Crear</h1>")

def post_detail(request):
	return HttpResponse("<h1>Ver</h1>")

def post_list(request):
	return render(request, "home.html", {})

def post_update(request):
	return HttpResponse("<h1>Modificar</h1>")

def post_delete(request):
	return HttpResponse("<h1>Eliminar</h1>")