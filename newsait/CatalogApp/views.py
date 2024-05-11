from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Products
from .serializers import ProductsSerializer

@csrf_exempt
def ProductApi(request, id = None):
    if request.method == 'GET':
        if id is not None:
            product = Products.objects.get(product_id=id)
            products_serializer = ProductsSerializer(product, many=False)
            return render(request, 'CatalogApp/main.html', {'products_serializer':[products_serializer.data]})
        else:
            return JsonResponse("404",safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        products_serializer=ProductsSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Успешно добавлен", safe=False)
        return JsonResponse("Не добавлен", safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Products.objects.get(product_id=product_data['product_id'])
        products_serializer = ProductsSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Успешно изменен", safe=False)
        return JsonResponse("Не изменен", safe=False)
    elif request.method == 'DELETE':
        product = Products.objects.get(product_id=id)
        product.delete()
        return JsonResponse("Удален", safe=False)