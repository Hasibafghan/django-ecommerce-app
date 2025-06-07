from django.shortcuts import render  , redirect , get_object_or_404 
from . models import Product , Category , Profile , Customer , Order
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm , UpdateUserForm , PasswordChangeForm , UpdateProfileForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q




def search_product(request):
    search_query = request.POST.get('search', '').strip()  # Get and clean the search term
    products = None  # Initialize products variable
    
    if request.method == 'POST' and search_query:  # Only search if there's a query
        products = Product.objects.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        ).distinct()  # Add distinct() to avoid duplicates
        
        if not products.exists():  # More efficient than 'if not products'
            messages.info(request, 'No products found matching your search.')
    
    context = {
        'search_query': search_query,  # The original search term
        'products': products,  # The filtered products
        'searched': bool(search_query)  # Flag indicating if a search was attempted
    }
    return render(request, 'search_product.html', context)




def update_info(request):
    if not request.user.is_authenticated:
        messages.error(request, 'First you must login')
        return redirect('login')

    try:
        current_user = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found')
        return redirect('products')  # or appropriate redirect
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('products')
    else:
        form = UpdateProfileForm(instance=current_user)
    
    return render(request, 'update_info.html', {'form': form})



def products(request):
    products = Product.objects.all()
    return render(request , 'index.html' , {'products': products})


def category_view(request):
    categories = Category.objects.all()
    return render(request , 'category_view.html' , {'categories' : categories})



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

def update_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        update_form = UpdateUserForm(request.POST or None , instance=user)
        if update_form.is_valid():
            update_form.save()
            login(request , user)
            messages.success(request , 'Profile updated successfully')
            return redirect('products')
        return render(request, 'update_user.html', {'form': update_form})
    else:
        messages.error(request, 'You need to be logged in to update your profile')
        return redirect('login')



def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = PasswordChangeForm(current_user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Prevents logout after password change
                messages.success(request, 'Password successfully changed')
                return redirect('products')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
                return render(request, 'update_password.html', {'form': form})
        else:
            form = PasswordChangeForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.error(request, 'You need to be logged in to change your password')
        return redirect('login')


def signup_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'Account created successfully')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

# signup success auto login
# def signup_user(request):
#     form = UserRegistrationForm()
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username = form.cleaned_data['username']
#             # password1 = form.cleaned_data['password1']
#             # user = authenticate(request, username=username, password=password1)
#             # login(request, user)
#             messages.success(request,"Done!")
#             return redirect('products')
#         else:
#             messages.error(request,"Error!")
#             return redirect('signup')   
#     else:
#         return render(request , 'signup.html' , {'form' : form})
    

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