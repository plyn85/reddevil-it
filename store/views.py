from django.shortcuts import render
from .models import Product


def shop(request):
    products.objects.all()
    context = {'products': products}
    return render(request, 'store/shop.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html')


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html')
