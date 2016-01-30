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
    url(r'^linkedin/check_response/(?P<code>\w*)$', views.linkedin_response_check, name='check_linkedin_response'),
    url(r'^facebook/$', views.facebook, name='facebook'),
    url(r'^facebook/check_response/(?P<code>\w*)$', views.facebook_response_check, name='check_facebook_response'),
]