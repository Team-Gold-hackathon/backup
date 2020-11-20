from django.db import models
from django.contrib.auth.models import User

#Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    city = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Baby and Child health', 'Baby and Child health'),
        ('Treatments and Medicaments','Treatments and Medicaments'),
        ('Treatments and Medicaments','Treatments and Medicaments'),
        ('First Aid','First Aid'),
        ('Sexual Wellbeing', 'Sexual Wellbeing', ),
        ('Personal Care', 'Personal Care'),

    )

    name =  models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category= models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url =self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, blank=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city  = models.CharField(max_length=200, null=False)
    state  = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.address
