from django.urls import path
from . import views

urlpatterns = [
    # Products
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),

    # Services
    path("services/", views.service_list, name="service_list"),
    path("services/new/", views.service_create, name="service_create"),

    # Raw Materials
    path("raw-materials/", views.raw_material_list, name="raw_material_list"),
    path("raw-materials/new/", views.raw_material_create, name="raw_material_create"),

]