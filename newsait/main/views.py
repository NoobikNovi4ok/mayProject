from django.db.models import Q
from django.shortcuts import render
from CatalogApp.models import Products, Categories, Countries
from django.core.paginator import Paginator
from main.utils import q_search
def index(request):
    products = Products.objects.all()[:4]
    context= {
        'products': products

    }
    return render(request, 'main/index.html',context)

def catalog(request):
    categories = Categories.objects.all()
    countries = Countries.objects.all()
    products = Products.objects.all()
    category_id = request.GET.getlist('category', 0)
    country_id = request.GET.getlist('country', 0)
    page = request.GET.get('page', 1)
    sort = request.GET.getlist('sort', None)
    query = request.GET.get('q', None)
    if query:
        products = q_search(query)
    if sort and 'd' not in sort:
        if 'DESC' in sort:
            if country_id and category_id:
                products = Products.objects.filter(
                    Q(category_id__in=category_id) & Q(country_id__in=country_id)).distinct().order_by('-cost')
            elif category_id:
                products = Products.objects.filter(category__in=category_id).distinct().order_by('-cost')
            elif country_id:
                products = Products.objects.filter(country__in=country_id).distinct().order_by('-cost')
            else:
                products = Products.objects.all().distinct().order_by('-cost')
        elif 'ASC' in sort:
            if country_id and category_id:
                products = Products.objects.filter(
                    Q(category_id__in=category_id) & Q(country_id__in=country_id)).order_by('cost')
            elif category_id:
                products = Products.objects.filter(category__in=category_id).order_by('cost')
            elif country_id:
                products = Products.objects.filter(country__in=country_id).order_by('cost')
            else:
                products = Products.objects.all().order_by('cost')
    else:
        if country_id and category_id:
            products = Products.objects.filter(
                Q(category_id__in=category_id) & Q(country_id__in=country_id))
        elif category_id:
            products = Products.objects.filter(category__in=category_id)
        elif country_id:
            products = Products.objects.filter(country__in=country_id)

    paginator = Paginator(products, 2)
    current_page = paginator.page(page)

    if sort:
        if category_id and country_id:
            country_id = [int(item) for item in country_id]
            category_id = [int(item) for item in category_id]
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select': category_id,
                'select_country': country_id,
                'select_sort': sort
            }
        elif category_id:
            category_id = [int(item) for item in category_id]
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select': category_id,
                'select_sort': sort
            }
        elif country_id:
            country_id = [int(item) for item in country_id]
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select_country': country_id,
                'select_sort': sort
            }
        else:
            print(current_page)
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select_sort': sort
            }
    else:
        if category_id and country_id:
            country_id = [int(item) for item in country_id]
            category_id = [int(item) for item in category_id]
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select': category_id,
                'select_country': country_id
            }
        elif category_id:
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select': category_id,
            }
        elif country_id:
            context = {
                'countries': countries,
                'category': categories,
                'products': current_page,
                'select_country': country_id,
            }
        else:
            context = {
                'countries': countries,
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
