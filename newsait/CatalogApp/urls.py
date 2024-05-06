from django.urls import path
from . import views

urlpatterns = [
    path(r'product', views.ProductApi),
    path(r'product/<int:id>', views.ProductApi)
]