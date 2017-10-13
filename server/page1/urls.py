from django.conf.urls import url

from .controller import controller

urlpatterns = [
    url(r'^$', controller.index, name='index'),
    url(r'^getallshops$', controller.select_all, name='getallshops$'),
    url(r'^get_products_from/(?P<shopId>[0-9]*)$', controller.select_product_from_shop, name='get_products_from'),
    url(r'^get_comments_from/(?P<shopId>[0-9]*)$', controller.get_comments_to_shop, name='get_comments_from'),
]
