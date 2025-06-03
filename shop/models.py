from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    data_modified = models.DateTimeField(User,auto_now=True)
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=200,blank=True, null=True)
    address2 = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    zip_code = models.CharField(max_length=20,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True , default='USA')

    def __str__(self):
        return f'{self.user.username} - {self.phone}'

def create_profile(sender, instance , created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)



class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=400 , default='No description' , blank=True , null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    image = models.ImageField(upload_to='upload/product/') 

    is_in_discount = models.BooleanField(default=False)
    discount = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    gave_star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f'{self.name} - {self.category}'
    

class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.customer} - {self.product}'