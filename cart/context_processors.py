from .cart import Cart

def cart_processor(request):
    """
    Context processor to add the cart and cart quantity to the context.
    """
    cart = Cart(request)
    return {
        'cart': cart,
        'cart_quantity': cart.total_quantity()
    }
