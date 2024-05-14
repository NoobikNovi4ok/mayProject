from django.shortcuts import render
from CatalogApp.models import Products, Categories, Countries
from django.core.paginator import Paginator
def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    categories = Categories.objects.all()
    category_id = request.GET.getlist('category', 0)
    if category_id:
        products = Products.objects.filter(category__in=category_id)
    else:
        products = Products.objects.all()

    paginator = Paginator(products, 6)
    current_page = paginator.page(1)

    if category_id:
        category_id = [int(item) for item in category_id]
        context = {
            'category': categories,
            'products': current_page,
            'select': category_id,
        }
    else:
        context = {
            'category': categories,
            'products': current_page,
        }

    return render(request, 'main/catalog.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def my_404_view(request, exception):
    context = {
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница была не найдена, или перемещена',
    }

    return render(request, 'main/404.html', context)
