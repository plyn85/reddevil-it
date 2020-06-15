from .models import Product, Order, OrderItem
from users.models import Profile
import json
from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal


def cart_contents(request):
    products = Product.objects.all()
    # if request.user.is_authenticated:

    #     profile = request.user.profile

    #     order, created = Order.objects.get_or_create(
    #         profile=profile, complete=False)

    #     cart_items = order.orderitem_set.all()

    #     grand_total = order.get_cart_total

    #     product_count = order.get_cart_items

    # else:
    try:
        cart = json.loads(request.COOKIES['cart'])
        print('CART:', cart)
    except:
        cart = {}

    cart_items = []

    product_count = 0
    total = 0

    # looping trough cart object and returning items plus the quantity of the entire cart
    for item, item_quantity in cart.items():
        product = Product.objects.get(id=item)
        item_quantity = cart[item]['quantity']
        total += item_quantity * product.price
        print(total)
        product_count += item_quantity
        print(product_count)

        cart_items.append({
            'id': product.id,
            'product': {'id': product.id, 'name': product.name, 'price': product.price,
                        'image': product.image}, 'quantity': cart[item]['quantity'], 'get_total': total,

        })

    if total < settings.FREE_DELIVERY_THRESHOLD and not request.user.is_authenticated:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        member_discount = 0
    if total > settings.FREE_DELIVERY_THRESHOLD and not request.user.is_authenticated:
        delivery = 0
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        member_discount = 0
    if request.user.is_authenticated and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        member_discount = total * Decimal(settings.MEMBER_DISCOUNT / 100)
    elif request.user.is_authenticated and total > settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0
        free_delivery_delta = 0
        member_discount = total * Decimal(settings.MEMBER_DISCOUNT / 100)

    # else:
    #     delivery = 0
    #     free_delivery_delta = 0
    #     member_discount = 0

    grand_total = delivery + total - member_discount

    context = {"cart_items": cart_items,
               "product_count": product_count, "total": total, 'delivery': delivery,  'free_delivery_delta': free_delivery_delta,
               'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
               'member_discount': member_discount,
               'grand_total': grand_total,
               'products': products,
               }

    return context
