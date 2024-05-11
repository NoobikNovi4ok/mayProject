from django.urls import path
from . import views

urlpatterns = [
    path(r'product/<int:id>', views.ProductApi),
]