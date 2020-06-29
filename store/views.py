
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Order, OrderItem
from django.contrib import messages
import stripe
from . contexts import cart_contents
from . forms import OrderForm
from django.views.generic import ListView, DetailView
from users.models import Profile
from users.forms import ProfileForm
from .filters import ProductFilter
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import json


class FilteredListView(ListView):
    """added from a tutorial found at https://www.caktusgroup.com/blog/
    2018/10/18/filtering-and-pagination-django/ used to allow django-filters 
    to be used with class based views used on  the ProductList view below """


    filterset_class = None

    def get_queryset(self):
        # getting the query set
        queryset = super().get_queryset()
        # then using the parameters to instantiate the filter set
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        # returning the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

        queryset = super().get_queryset()
        # then using the parameters to instantiate the filter set
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        # returning the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class ProductListView(FilteredListView):
    """ renders all products on the shop page using products model in 
    ordered by price posted paginted so 8 products shown at a 
    time, filterlistview passed in from above to allow django
    filters products filter to be filterset class passed into the 
    shop page  """
    filterset_class = ProductFilter
    model = Product
    # changing the default page where the list views looks for template
    template_name = 'store/shop.html'
    context_object_name = "products"
    ordering = ['price']
    paginate_by = 8


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/product_detail.html', context)


def shop(request):
    """ view renders the shop page """

    context = {
        'products': products,


    }

    return render(request, 'store/shop.html', )


def cart(request):
    """ view renders the cart page """

    return render(request, 'store/cart.html')


def checkout(request):
    """ view handles checkout an payment using stripe
    if its as post request orderform data an orderitems are 
    saved to the database. The user is then redirected to 
    the checkout success page. If its a get request the 
    order form is rendered with an attempt made to prefill 
    the form with any existing user information """

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
        # total taken from cart contents method context here
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
    """ transaction id passed from checkout view here used 
    to get the order if its a logged In user the order Is attached to the 
    profile and saved. The users order Infomation is then passed
    into the profile form and saved finally the cookie which contained 
    the cart is deleted """
   

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
    
    # Send the user a confirmation email
    
    email = order.email
    subject = render_to_string(
            'email_confirm/email_confirm_subject.txt',)
    body = render_to_string(
            'email_confirm/email_confirm.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,
            )

    
    response = render(request, 'store/checkout_success.html', context)
    # remove cart from cookies when checkout success page reached
    response.delete_cookie("cart")
    return response


    
    
    