from django.urls import path
from CatalogApp.views import ProductApi

urlpatterns = [
    path(r'<slug:slug>', ProductApi),
]