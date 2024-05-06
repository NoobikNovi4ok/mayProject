from django.shortcuts import render
from CatalogApp.models import Products
def index(request):
    return render(request, 'main/index.html')

def catalog(request):
      context = {
          'products': Products.objects.all()
      }
      return render(request, 'main/catalog.html',context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

