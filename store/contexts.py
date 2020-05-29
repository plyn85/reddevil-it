from .models import Product, Order, OrderItem
from django.conf import settings


def cart_contents(request):
    if request.user.is_authenticated:
        customer = request.user.customer
    # creating or getting the order item
        order, created = Order.  objects.get_or_create(
            customer=customer, complete=False)
    # getting the items attached to the order
    # getting all order items that have the order as the parent
        items = order.orderitem_set.all()
    # getting all cart Items passing it into context
        cartItems = order.get_cart_items
    # if user is not logged in return an empty list
    else:

        items = []
        # setting empty cart for users who are not logged In
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        # setting empty Items for users who are not logged In
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}

    return context
