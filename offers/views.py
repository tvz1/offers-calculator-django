from django.shortcuts import render, redirect
from .models import Product, Service, RawMaterial
from .forms import ProductForm, ServiceForm, RawMaterialForm


# Product views
def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "product_form.html", {"form": form})


# Service views
def service_list(request):
    services = Service.objects.all()
    return render(request, "service_list.html", {"services": services})


def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service_list")
    else:
        form = ServiceForm()

    return render(request, "service_form.html", {"form": form})

# RawMaterial views
def raw_material_list(request):
    materials = RawMaterial.objects.all()
    return render(request, "raw_material_list.html", {"materials": materials})


def raw_material_create(request):
    if request.method == "POST":
        form = RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("raw_material_list")
    else:
        form = RawMaterialForm()

    return render(request, "raw_material_form.html", {"form": form})
