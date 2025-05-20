from django.shortcuts import render  , redirect
from . models import Product , Category , Customer , Order
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.urls import reverse_lazy


def products(request):
    products = Product.objects.all()
    return render(request , 'index.html' , {'products': products})


def about_us(request):
    return render(request , 'about.html')


def login_user(request):
    return render(request , 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request , 'Logout successfully')
    return redirect('products')