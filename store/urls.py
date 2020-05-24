from django.urls import path
from .views import cart, checkout, shop

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

]
