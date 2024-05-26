from django.http import JsonResponse
from django.shortcuts import render, redirect
from CatalogApp.models import Products
from basket.models import Basket
from django.template.loader import render_to_string
from basket.utils import get_user_basket


def basket_add(request):
    product_id = request.POST.get("product_id")
    product = Products.objects.get(product_id=product_id)

    baskets = Basket.objects.filter(user=request.user,product=product)

    if baskets.exists():
        basket = baskets.first()
        if basket:
            basket.quantity += 1
            basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    user_basket = get_user_basket(request)
    cart_items_html = render_to_string(
        "basket/includes/included_cart.html", {'basket': user_basket}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)

def basket_change(request):
    basket_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    basket = Basket.objects.get(basket_id=basket_id)

    basket.quantity = quantity
    basket.save()
    updated_quantity = basket.quantity

    user_basket = get_user_basket(request)
    cart_items_html = render_to_string(
        "basket/includes/included_cart.html", {'basket': user_basket}, request=request
    )

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def basket_remove(request):
    basket_id = request.POST.get("cart_id")
    basket = Basket.objects.get(basket_id=basket_id)
    quantity = basket.quantity
    basket.delete()

    user_basket = get_user_basket(request)
    cart_items_html = render_to_string(
        "basket/includes/included_cart.html", {'basket': user_basket}, request=request
    )

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)