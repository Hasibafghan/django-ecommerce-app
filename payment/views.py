from django.shortcuts import render


def payment(request):
    """
    Render the payment page.
    """
    return render(request, 'payment/payment_success.html')