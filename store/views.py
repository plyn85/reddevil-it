from django.shortcuts import render
from .models import Product, Order


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        #    getting the customer
        customer = request.user.customer
        # creating or getting the order item
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # getting the items attached to the order
        # getting all order items that have the order as the parent
        items = order.orderitem_set.all()
    # if user is not logged in return an empty list
    else:
        items = []
        # setting empty cart for users who are not logged In
    order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):

    context = {}
    return render(request, 'store/checkout.html')
