from rest_framework import serializers
from .models import Products, Countries, Categories

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id','name','slug','photo','description','quantity','cost','country','nutritional_value','manufactures','category')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('country_id', 'name', 'slug')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category_id','name','slug')
