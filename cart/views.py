from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product , Profile


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for item_id, quantity in cart.items():
        try:
            # Ensure item_id is valid integer for Product lookup
            product = get_object_or_404(Product, pk=int(item_id))
            # Convert quantity to integer
            quantity = int(quantity)
            if quantity <= 0:
                continue  # skip invalid or zero-quantity items
            # Choose correct price
            unit_price = product.discount if product.is_in_discount else product.price
            # Calculate totals
            total = unit_price * quantity
            total_price += total
            # Append item details to the cart list
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'unit_price': unit_price,
                'total_price': total
            })
        except (ValueError, TypeError):
            # Skip items with invalid ID or quantity
            continue
    return render(request, 'cart_view.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


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
    cart = request.session.get('cart', {})
    if item_id in cart:
        del cart[item_id]
        request.session['cart'] = cart
    return redirect('view_cart')

def update_cart_item(request, item_id):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if item_id in cart:
            if quantity > 0:
                cart[item_id] = quantity
            else:
                del cart[item_id]
        
        request.session['cart'] = cart
        return redirect('view_cart')
    else:
        return render(request, 'cart_view.html', {'item_id': item_id})
