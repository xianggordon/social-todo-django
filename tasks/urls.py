from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'up', views.say_whatsup, name='whatsup'),
    url(r'^newTask', views.newTask, name='newTask'),
    url(r'^delete/(?P<task_id>[0-9]+)/$', views.deleteTask, name='delete'),
    url(r'^toggle/(?P<task_id>[0-9]+)/$', views.toggleTask, name='toggle'),
]

