from django.shortcuts import render


def shop(request):
    context = {}
    return render(request, 'store/shop.html')


def cart(request):
    context = {}
    return render(request, 'store/cart.html')


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html')
