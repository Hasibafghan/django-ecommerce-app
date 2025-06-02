class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def total_quantity(self):
        """
        Safely sums up item quantities in the cart,
        converting string values to integers and skipping invalid ones.
        """
        return sum(
            int(qty) for qty in self.cart.values()
            if qty is not None and str(qty).isdigit()
        )
