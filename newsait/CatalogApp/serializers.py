from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id','name','slug','photo','description','cost','country','nutritional_value','manufactures','category')