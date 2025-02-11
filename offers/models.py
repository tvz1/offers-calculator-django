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

class Offer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Offer {self.id} for {self.customer.name}"
    
class OfferItem(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        if self.product:
            return f"{self.quantity} x {self.product.name}"
        elif self.service:
            return f"{self.quantity} x {self.service.name}"
        elif self.raw_material:
            return f"{self.quantity} x {self.raw_material.name}"
        else:
            return "Invalid Item"
