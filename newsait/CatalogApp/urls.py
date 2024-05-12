from django.urls import path
from . import views

urlpatterns = [
    path(r'product/<str:slug>', views.ProductApi),
]