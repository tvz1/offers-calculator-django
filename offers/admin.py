from django.contrib import admin
from .models import Customer,Product,Service,RawMaterial

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(RawMaterial)

