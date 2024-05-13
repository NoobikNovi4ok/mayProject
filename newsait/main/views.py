from django.shortcuts import render
from CatalogApp.models import Products, Categories, Countries
def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    categories = Categories.objects.all()
    category_id = request.GET.getlist('category', 0)
    if category_id:
        products = Products.objects.filter(category__in=category_id)
    else:
        products = Products.objects.all()

    if category_id:
        category_id = [int(item) for item in category_id]
        context = {
            'category': categories,
            'products': products,
            'select': category_id,
        }
    else:
        context = {
            'category': categories,
            'products': products
        }

    return render(request, 'main/catalog.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

