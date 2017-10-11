from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.post_list), name='home'),
    url(r'^create/$', login_required(views.post_create), name='create'),
    url(r'^(?P<id>[\w-]+)/$', login_required(views.post_detail), name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', login_required(views.post_update), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', login_required(views.post_delete), name='delete'),
]