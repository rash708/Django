from django.conf.urls import url
from ecomapp.views import base_view, category_view, product_view, cart_view, add_to_cart, remove_from_cart

urlpatterns = [
	url(r'^$', base_view, name='base'),
	url(r'^cart/$', cart_view, name='cart'),
	url(r'^remove_from_cart/(?P<product_slug>[-\w]+)/s', remove_from_cart, name='remove_from_cart'),
	url(r'^add_to_cart/(?P<product_slug>[-\w]+)/s', add_to_cart, name='add_to_cart'),
	url(r'^category/(?P<category_slug>[-\w]+)/s', category_view, name='category_detail'),
	url(r'^product/(?P<product_slug>[-\w]+)/s', product_view, name='product_detail'),
]
