from django.conf.urls import url

from users.views import RegisterUser

urlpatterns = [
	url(r'^register', RegisterUser.as_view(), name='register'),
]