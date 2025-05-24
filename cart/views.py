from django.shortcuts import render


def view_cart(request):
    return render(request , 'cart_view.html' , {})


def add_to_cart(request):
    pass


def remove_from_cart(request, item_id):
    pass

def update_cart_item(request, item_id):
    pass