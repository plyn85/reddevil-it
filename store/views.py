from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Order, OrderItem
from django.http import JsonResponse
import json
from django.conf import settings
from django.contrib import messages
import stripe
from . contexts import cart_contents
from . forms import OrderForm
from django.views.generic import ListView, DetailView
from users.models import Profile
from users.forms import ProfileForm


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


class ProductDetailView(DetailView):
    # adding post model
    model = Product


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
        cart = json.loads(request.COOKIES['cart'])
        if not cart:
            messages.warning(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('shop'))

        cart_total = cart_contents(request)
        total = cart_total["grand_total"]
        stripe_total = total
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY)

        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
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

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.profile = profile
        order.save()

        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = ProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    context = {"order": order}
    response = render(request, 'store/checkout_success.html', context)
    # remove cart from cookies when checkout success page reached
    response.delete_cookie("cart")
    return response


# def updateItem(request):
#     # getting data sent In from cart.js
#     data = json.loads(request.body)
#     # querying the data an getting the values
#     productId = data['productId']
#     action = data['action']
#     print('action:', action)
#     print('productId:', productId)

#     customer = request.user.profile
#     product = Product.objects.get(id=productId)

#     order, created = Order.objects.get_or_create(
#         profile=customer, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(
#         order=order, product=product)
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)
#     # saving orderitem to cart
#     orderItem.save()
#     # delete order item if none remain
#     if orderItem.quantity <= 0:
#         orderItem.delete()

#     return JsonResponse('item was added', safe=False)
