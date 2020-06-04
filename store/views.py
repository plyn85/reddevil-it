from django.shortcuts import render
from .models import Product, Order, OrderItem
from django.http import JsonResponse
import json
from django.conf import settings
import stripe
from . contexts import cart_contents
from . forms import CustomerForm, ShippingForm


def shop(request):

    return render(request, 'store/shop.html')


def cart(request):

    return render(request, 'store/cart.html')


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # setting cuttent cart to imported cart_contents method
    current_cart = cart_contents(request)
    total = current_cart['cart_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    customer_form = CustomerForm()
    shipping_form = ShippingForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe Public key Is Missing!')

    context = {
        'customer_form': customer_form,
        'shipping_form': shipping_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
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
