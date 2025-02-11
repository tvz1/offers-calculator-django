from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Product, Service, RawMaterial, Offer, OfferItem
from .forms import ProductForm, ServiceForm, RawMaterialForm, OfferForm, OfferItemForm


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


# Offer views
def offer_list(request):
    offers = Offer.objects.all()
    return render(request, "offer_list.html", {"offers": offers})


def offer_create(request):
    OfferItemFormSet = formset_factory(OfferItemForm, extra=5)

    if request.method == "POST":
        form = OfferForm(request.POST)
        formset = OfferItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            offer = form.save(commit=False)  # commit=False -> nemoj spremiti u bazu
            offer.save()

            total_cost = 0
            for offer_item in formset:
                product = offer_item.cleaned_data.get("product")
                service = offer_item.cleaned_data.get("service")
                raw_material = offer_item.cleaned_data.get("raw_material")
                quantity = offer_item.cleaned_data.get("quantity")

                if product or service or raw_material:
                    if product:
                        cost = product.base_price * quantity
                    elif service:
                        cost = service.service_rate * quantity
                    elif raw_material:
                        cost = raw_material.unit_price * quantity

                    total_cost += cost

                    OfferItem.objects.create(
                        offer=offer,
                        product=product,
                        service=service,
                        raw_material=raw_material,
                        quantity=quantity,
                        cost=cost,
                    )

            offer.total_cost = total_cost
            offer.save()

            return redirect("offer_list")
    else:
        form = OfferForm()
        formset = OfferItemFormSet()

    return render(request, "offer_form.html", {"form": form, "formset": formset})

def offer_detail(request, pk):
    offer = Offer.objects.get(pk=pk)
    items = OfferItem.objects.filter(offer=offer)
    return render(request, "offer_detail.html", {"offer": offer, "items": items})
