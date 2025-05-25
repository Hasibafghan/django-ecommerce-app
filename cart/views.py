from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total = product.price * quantity
        total_price += total
        cart_items.append({'product': product, 'quantity': quantity, 'total_price': total})

    return render(request, 'cart_view.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if item_id in cart:
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
        return redirect('view_cart')
    else:
        return render(request, 'add_to_cart.html')

def remove_from_cart(request, item_id):
    pass

def update_cart_item(request, item_id):
    pass
