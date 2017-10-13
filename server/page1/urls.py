from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getallshops$', views.select_all, name='getallshops$'),
    url(r'^get_products_from/(?P<shopId>[0-9]*)$', views.select_product_from_shop, name='get_products_from'),
    url(r'^get_comments_from/(?P<shopId>[0-9]*)$', views.get_comments_to_shop, name='get_comments_from'),

]