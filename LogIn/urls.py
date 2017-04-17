from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'LogIn/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'LogIn/login.html'}, name='logout'),
    url(r'^register/$', CreateView.as_view(
        template_name='LogIn/register.html',
        form_class=UserCreationForm,
        success_url='/login/success',
    ), name='register'),
    url(r'^success/$', views.register_success, {'template_name': 'LogIn/success.html'},
        name='register_success'),
]