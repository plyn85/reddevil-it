from django.urls import path
from .views import cart, checkout, ProductListView, product_detail, checkout_success

urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shop'),
    path('<int:product_id>/', product_detail, name='product-detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    # path('update_item/', update_item, name='update-item'),
    path('checkout_success/<transaction_id>',
         checkout_success, name='checkout_success'),

]
