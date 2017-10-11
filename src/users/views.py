# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from users.forms import RegisterForm
# Create your views here.
class RegisterUser(CreateView):
	model = User
	template_name = "users/register.html"
	form_class = RegisterForm
	success_url = reverse_lazy('posts:home')