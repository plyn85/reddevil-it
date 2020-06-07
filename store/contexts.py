from .models import Product, Order, OrderItem
from users.models import Profile
import json
from django.shortcuts import get_object_or_404


def cart_contents(request):

    if request.user.is_authenticated:
        # getting users profile an passing into get or create
        profile = request.user.profile

        order = Order.objects.get(profile=profile)
    # getting the items attached to that order
        items = order.orderitem_set.all()
    # getting cart total
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
        # setting empty Items for users who are not logged In
        # setting empty cart for users who are not logged In
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    # looping trough cart object and returning items plus the quantity of the entire cart
        for i in cart:
            cartItems += cart[i]['quantity']
    # getting product Id
            product = Product.objects.get(id=i)
    # getting cart total
            total = (product.price * cart[i]['quantity'])
    # adding cart total an quantity to order dict from above
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
    #  creating repersentation of cart Items
            item = {
                'id': product.id,
                'product': {'id': product.id, 'name': product.name, 'price': product.price,
                            'image': product.image}, 'quantity': cart[i]['quantity'],

            }
    #  adding item to items list
            items.append(item)

    products = Product.objects.all()

    # creating or getting the order item

    #  getting cart total amount
    # obj = OrderItem.objects.get_cart_total()
    # cart_total = obj
    context = {'items': items, 'products': products,
               'cartItems': cartItems, 'order': order}

    return context
