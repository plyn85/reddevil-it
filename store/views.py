from django.shortcuts import render
from .models import Product, Order, OrderItem
from django.http import JsonResponse
import json
from django.conf import settings
import stripe
from . contexts import cart_contents
from . forms import OrderForm


def shop(request):

    return render(request, 'store/shop.html')


def cart(request):

    return render(request, 'store/cart.html')


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],

        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()

    else:

        # setting cuttent cart to imported cart_contents method
        profile = request.user.profile
        order, created = Order.objects.get_or_create(
            profile=profile, complete=False)
        # getting cart total
        total = order.get_cart_total

        stripe_total = total
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY)

        order_form = OrderForm()
        if not stripe_public_key:
            messages.warning(request, 'Stripe Public key Is Missing!')

        context = {
            'order_form': order_form,
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
    customer = request.user.profile
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(
        profile=customer, complete=False)

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
