from django.shortcuts import render
from django.contrib import messages
from .models import Payment_info
from .forms import PaymentForm
from shop.models import Profile
from django.shortcuts import redirect


def payment(request):
    """
    Render the payment page.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'First you must login')
        return redirect('login')

    try:
        current_user = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found')
        return redirect('products')  # or appropriate redirect

    try:
        payment_info = Payment_info.objects.get(user=request.user)
    except Payment_info.DoesNotExist:
        payment_info = Payment_info(user=request.user)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment information updated successfully!')
            return redirect('products')
    else:
        form = PaymentForm(instance=payment_info)

    return render(request, 'payment/payment_info.html', {'form': form, 'current_user': current_user})
