from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'up', views.say_whatsup, name='whatsup'),
    url(r'^newTask', views.newTask, name='newTask'),
    url(r'^delete/(?P<task_id>[0-9]+)/$', views.say_whatsup, name='delete'),
    # url(r'^delete/2', views.delete, name='whatsup'),
]

