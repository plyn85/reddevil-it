from django.shortcuts import render
from .models import Product, Order, OrderItem
from django.http import JsonResponse
import json


def shop(request):

    return render(request, 'store/shop.html')


def cart(request):

    return render(request, 'store/cart.html')


def checkout(request):
    context = {
        'stripe_public_key': 'pk_test_OtuMpmziQFrVOnItNeA1NK8n00Pdyae7Qg',
        'client_secret': 'test client secret'
    }
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
