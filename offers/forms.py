from django import forms
from .models import Product,Service,RawMaterial


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","description","base_price"]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name","description","service_rate"]

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = ["name", "description", "unit_price", "quantity_in_stock"]
        # fields = "__all__"