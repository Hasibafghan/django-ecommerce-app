from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Payment_info(models.Model):
    """
    Model to represent a payment.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=200,blank=True, null=True)
    address2 = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True , default='USA')
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    zip_code = models.CharField(max_length=20,blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Payment Information'
        verbose_name_plural = 'Payment Information'

    def __str__(self):
        return f"{self.full_name} - {self.amount} {self.currency} - {self.status}"
    


# class Order(models.Model):
#     user = models. ForeignKey(User, on_delete=models. CASCADE, null=True, blank=True)
#     full_name = models.CharField(max_length=250)
#     email = models. EmailField(max_length=300)
#     shipping_address = models.TextField(max_length=500, blank=True, null=True)
#     amount_paid = models.DecimalField(decimal_places=0 , max_digits=12)
#     date_ordered = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Order - {self.id} by {self.full_name} on {self.date_ordered.strftime("%Y-%m-%d %H:%M:%S")}'
    

# class OrderItem(models.Model):
#     order = models. ForeignKey(Order, on_delete=models. CASCADE, null=True)
#     products = models. ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, nul1=True)
#     quantity = models.PositiveIntegerField(default = 1)
#     price = models. DecimalField(decimal_places=2, max_digits=12)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Order Item - {self.id} for Order - {self.order.id}'