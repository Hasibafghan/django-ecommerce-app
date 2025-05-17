from django.db import models



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


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=400 , default='No description' , blank=True , null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    image = models.ImageField(upload_to='upload/product/') 

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