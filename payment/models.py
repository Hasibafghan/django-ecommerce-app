from django.db import models
from django.contrib.auth.models import User



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