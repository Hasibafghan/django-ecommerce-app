from django.shortcuts import render  , redirect , get_object_or_404 
from . models import Product , Category , Customer , Order
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import UserRegistrationForm


def products(request):
    products = Product.objects.all()
    return render(request , 'index.html' , {'products': products})


def about_us(request):
    return render(request , 'about.html')


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
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request , 'Logout successfully')
    return redirect('products')


# def signup_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request , 'Account created successfully')
#             return redirect('login')
#         else:
#             messages.error(request , 'Error creating account')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'signup.html', {'form': form})

# signup success auto login
def signup_user(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password1 = form.cleaned_data['password1']
            # user = authenticate(request, username=username, password=password1)
            # login(request, user)
            messages.success(request,"Done!")
            return redirect('products')
        else:
            messages.error(request,"Error!")
            return redirect('signup')   
    else:
        return render(request , 'signup.html' , {'form' : form})
    

def product_detail(request,pk):
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    return render(request , 'product_detail.html' , {'product': product})


def category_products(request, category_name):
    try:
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        return render(request , 'category_products.html' , {'products': products , 'category': category})
    except Category.DoesNotExist:
        messages.error(request , 'Category not found')
        return redirect('products')