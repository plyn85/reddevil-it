from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Order, OrderItem
from django.http import JsonResponse
import json
from django.conf import settings
import stripe
from . contexts import cart_contents
from . forms import OrderForm
from django.views.generic import ListView


def shop(request):

    products = Product.objects.all()
    context = {"products": products}

    return render(request, 'store/shop.html', context)


class ProductListView(ListView):

    model = Product
    # changing the default page where the list views looks for template
    template_name = 'store/shop.html'
    context_object_name = "products"
    ordering = ['price']
    paginate_by = 5


def shop(request):

    products = Product.objects.all()
    context = {"products": products}

    return render(request, 'store/shop.html', context)


def cart(request):

    return render(request, 'store/cart.html')


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = json.loads(request.COOKIES['cart'])

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
            # looping trough cart object and returning items plus the quantity of the entire cart
            for item, item_quantity in cart.items():
                product = Product.objects.get(id=item)
                item_quantity = cart[item]['quantity']
                order_item = OrderItem(
                    order=order, product=product, quantity=item_quantity)
                order_item.save()

            return redirect(reverse('checkout_success', args=[order.transaction_id]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart_total = cart_contents(request)
        total = cart_total["grand_total"]
        stripe_total = total
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY)

        order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe Public key Is Missing!')
    template = 'store/checkout.html'
    context = {

        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, transaction_id):

    order = get_object_or_404(Order, transaction_id=transaction_id)
    context = {"order": order}
    response = render(request, 'store/checkout_success.html', context)
    # remove cart from cookies when checkout success page reached
    response.delete_cookie("cart")
    return response


def updateItem(request):
    # getting data sent In from cart.js
    data = json.loads(request.body)
    # querying the data an getting the values
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

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
