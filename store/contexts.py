from .models import Product, Order, OrderItem
import json


def cart_contents(request):

    if request.user.is_authenticated:
        customer = request.user.customer
    # creating or getting the order item
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    # getting the items attached to the order
    # getting all order items that have the order as the parent
        items = order.orderitem_set.all()
    #  getting cart tottal amount
        cart_total = order.get_cart_total
    #  getting cart total items
        cartItems = order.get_cart_items
    # if user is not logged in return cart cookie
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        # if theres no cookie return an empty cart object
        except:
            cart = {}
        print('CART:', cart)

        items = []
        # setting empty cart for users who are not logged In
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        # setting empty Items for users who are not logged In
        cartItems = order['get_cart_items']
    # looping trough cart object and returning items plus the quantity of the entire cart
    for i in cart:
        cartItems += cart[i]['quantity']

    products = Product.objects.all()

    context = {'items': items, 'products': products,
               'cartItems': cartItems, 'order': order, }

    return context
