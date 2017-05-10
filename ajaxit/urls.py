from django.conf.urls import url
from django.contrib import admin
from ajaxit import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajaxit/addemployee/$', views.addemployee, name='addemployee'),
    url(r'^ajaxit/delemployee/$', views.delemployee, name='delemployee'),
    url(r'^ajaxit/editemployee/$', views.editemployee, name='editemployee'),
    url(r'^ajaxit/editemployeefull/$', views.editemployeefull, name='editemployeefull'),

]