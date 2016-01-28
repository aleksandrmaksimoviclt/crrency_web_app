from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.index, name='login'),
    url(r'^basic/$', views.basic, name='basic'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/user_create/$', views.user_create, name='new_user'),
    url(r'^user/(?P<user_id>\d+)/activate/$', views.activate, name='activate'),
#social auth
    url(r'^linkedin/$', views.linkedin, name='linkedin'),
    url(r'^linkedin/check_response/(?P<code>\w*)$', views.check_redirect_response, name='check_linkedin_response'),
]