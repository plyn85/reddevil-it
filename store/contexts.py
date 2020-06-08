from .models import Product, Order, OrderItem
from users.models import Profile
import json
from django.shortcuts import get_object_or_404


def cart_contents(request):

    if request.user.is_authenticated:

        profile = request.user.profile

        order, created = Order.objects.get_or_create(
            profile=profile, complete=False)

        cart_items = order.orderitem_set.all()

        grand_total = order.get_cart_total

        product_count = order.get_cart_items

    else:
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
        grand_total = total
        print(grand_total)
        # print(cart_items)

    context = {"cart_items": cart_items,
               "product_count": product_count, "grand_total": grand_total, }

    return context
