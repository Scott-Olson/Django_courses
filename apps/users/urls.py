from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^users/(?P<id>\d+)/destroy$', views.userDelete),
	url(r'^users/(?P<id>\d+)/edit$', views.userEdit),
	url(r'^users/(?P<id>\d+)$', views.user),
	url(r'^users/new$', views.userNew),
	url(r'^users/create$', views.userCreate),
	url(r'^users/update$', views.userUpdate),
	url(r'^users', views.userslist),
	url(r'^', views.landing),
]