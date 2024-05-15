from django.urls import path
from . import views

urlpatterns = [
    path(r'<slug:slug>', views.ProductApi),
]