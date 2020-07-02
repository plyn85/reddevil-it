from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileForm, UserPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile
from fourm.models import Post
from store.models import Order, OrderItem
from django.contrib.auth.views import LoginView
import json


class MyLoginView(LoginView):
    """if the users cart is empty returns the user
       there the profile page on login if the users has items In the cart returns the user to the shop on login"""

       
    def get_success_url(self):
        
        try:
            cart = json.loads(self.request.COOKIES['cart'])
            if cart:
                messages.info(self.request, f'Your cart contains Items!')
                url = self.get_redirect_url()
                return url or reverse('shop')
        except:
            cart ={}
    
            messages.info(self.request, f'Welcome too Your profile page!')
            return reverse('profile')


def register(request):
    """ If a post request is made and the form is valid the user 
    is brought to the login page. If Its a get request form is rendered 
    and the register page"""
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """profile veiw handels two forms which update the users
    personal and deliver infomation both redirect to proifle
    page after successful post request a get request renders 
    the two forms along with the users order history"""
    
    profile = get_object_or_404(Profile, user=request.user)
    # update user form
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            
            messages.success(
                request, f'{request.user.username} Your account has been Updated!')
            return redirect('profile')
     # update profile form
    if request.method == "POST":
        p_form = ProfileForm(
            request.POST, instance=profile)
        if p_form.is_valid():
            p_form.save()

            messages.success(
                request, f'{request.user.username} Your account has been Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        orders = profile.orders.all
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'orders': orders,

    }
    return render(request, 'users/profile.html', context)


def change_password(request):
    """ view allows the user to change there current password
    if a successful post request is made there password is changed 
    and they are returned to there profile page If a get request is 
    made the password change form is rendered and change password page"""
    
    profile = get_object_or_404(Profile, user=request.user)
    # password from
    if request.method == 'POST':
        pass_change_form = UserPasswordChangeForm(request.user, request.POST)
        if pass_change_form.is_valid():
            user = pass_change_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        pass_change_form = UserPasswordChangeForm(request.user)

    return render(request, 'users/change_password.html', {
        'pass_change_form': pass_change_form
    })


def order_history(request, transaction_id):
    """ order history view passes the order to the checkout success 
    page. If tghe user has come from there profile page gives user 
    abilty to return there by passing from profile as true """
    
    order = get_object_or_404(Order, transaction_id=transaction_id)
    template = 'store/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
