from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    adress = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True) #optional
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True) #optional
    service_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

#TODO:Offers