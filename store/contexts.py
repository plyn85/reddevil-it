from .models import Product, Order, OrderItem
from users.models import Profile
import json
from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal


def cart_contents(request):
    """cart contents context cart and delivery infomation avaiable 
    across all pages. Get the json cart converts to a python object
    loops trough the cart appending to the cart items list if the
    total is less less then the deilvery treshold the deilvery cost 
    is summed and added"""
    products = Product.objects.all()[:8]

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    cart_items = []
    product_count = 0
    total = 0

    # looping trough cart object and returning items plus the quantity of the entire cart
    for item, item_quantity in cart.items():
        # try block to prevent items in cart that may have been removed from causing error
        try:
            product = Product.objects.get(id=item)
            item_quantity = cart[item]['quantity']
            total += item_quantity * product.price
            product_count += item_quantity
            cart_items.append({
                'id': product.id,
                'product': {'id': product.id, 'name': product.name, 'price': product.price,
                              'image': product.image}, 'quantity': cart[item]['quantity'], 'get_total': total,
            })
        except:
            pass
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    grand_total = delivery + total
    context = {"cart_items": cart_items,
               "product_count": product_count, "total": total, 'delivery': delivery,  'free_delivery_delta': free_delivery_delta,
               'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
               'grand_total': grand_total,
               'products': products,

               }

    return context
