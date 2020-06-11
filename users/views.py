from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileForm
from .models import Profile
from fourm.models import Post
from store.models import Order


def register(request):
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
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=profile)
        p_form = ProfileForm(
            request.POST, instance=profile)
        # both forms have to be valid to save the data
        if u_form.is_valid() and p_form.is_valid():

            u_form.save()
            p_form.save()

            messages.success(
                request, f'{request.user.username} Your account has been Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=profile)
        # orders = profile.orders.all()
        # print(orders)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
