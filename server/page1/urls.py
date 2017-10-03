from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getallshops$', views.select_all, name='getallshops$'),
    #url(r'^(?P<query>[A-Za-z0-9_-]+)/results$', views.select_all, name='select_all'),

]