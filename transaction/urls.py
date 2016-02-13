from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_transactions, name='transactions'),
    url(r'^make/$', views.make_transaction, name='transact'),
      
]