from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    emil=models.EmailField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

    
class Product(models.Model):

    CATEGORY = (
        ('Indoor','indoor'),
        ('out Door','out Door'),
    )

    name= models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True, choices=CATEGORY)
    description=models.CharField(max_length=200,null=True ,blank=True)
    data_created=models.DateTimeField(auto_now_add=True ,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    data_created=models.DateTimeField(auto_now_add=True ,null=True)
    status=models.CharField(max_length=200,null=True ,choices=STATUS)
    def __str__(self):
        return self.product.name
    
