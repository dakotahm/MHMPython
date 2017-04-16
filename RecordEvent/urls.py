from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name='Collect'),
    url(r'^AddMeasurable/',views.insertMeasurable, name='Measurables'),
]