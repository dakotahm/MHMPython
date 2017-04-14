from django.conf.urls import url
from django.contrib import admin
from . import views



from .views import get_data, ChartData

urlpatterns=[
    url(r'^$',views.DisplayView, name='DisplayView'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view())
]