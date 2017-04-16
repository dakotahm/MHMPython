from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    url(r'^$', views.login, {'template_name': 'LogIn/Login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'LogIn/Login.html'}, name='logout'),
]