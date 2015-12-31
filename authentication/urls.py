from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.index, name='login'),
    url(r'^basic/$', views.basic, name='basic'),
    url(r'^register/$', views.register, name='register'),
]