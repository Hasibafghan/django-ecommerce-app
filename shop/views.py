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


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request , username = username , password = password)
#         if user is not None:
#             login(request , user)
#             messages.success(request , 'login successfully')
#             redirect('products')
#         else:
#             messages.success(request , 'login has problem')
#             redirect('login')
#     return render(request , 'login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request , 'login successfully')
            return redirect('products')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_user')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request , 'Logout successfully')
    return redirect('products')