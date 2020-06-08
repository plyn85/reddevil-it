from django.urls import path
from .views import cart, checkout, shop, updateItem as update_item, checkout_success

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name='update-item'),
    path('checkout_success/', checkout_success, name='checkout_success'),


]
