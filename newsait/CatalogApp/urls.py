from django.urls import path
from . import views
from .models import Products

urlpatterns = [
    path(r'<slug:slug>', views.ProductApi),
]