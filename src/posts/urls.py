from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>[\w-]+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', views.post_delete),
]