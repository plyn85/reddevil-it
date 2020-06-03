from django.urls import path
from .views import cart, checkout, shop, updateItem as update_item

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name='update-item'),

]
