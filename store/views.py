from django.shortcuts import render
from .models import Product, Order, OrderItem
from django.http import JsonResponse
import json


def shop(request):

    products = Product.objects.all()

    return render(request, 'store/shop.html')


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
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    # getting data sent In from cart.js
    data = json.loads(request.body)
    # qureying the data an getting the values
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

# getting customer and productId
    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    # saving orderitem to cart
    orderItem.save()
    # delete order item if none remain
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)
