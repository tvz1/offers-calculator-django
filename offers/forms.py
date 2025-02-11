from django import forms
from .models import Product,Service,RawMaterial,Offer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","description","base_price"]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name","description","service_price"]

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = ["name", "description", "unit_price", "quantity_in_stock"]
        # fields = "__all__"

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ["customer","valid_until"]
        widgets = {
            "valid_until":forms.DateInput(attrs={"type":"date"}),
        }


class OfferItemForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    raw_material = forms.ModelChoiceField(
        queryset=RawMaterial.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    quantity = forms.IntegerField(
        min_value=1, widget=forms.NumberInput(attrs={"class": "form-control"})
    )