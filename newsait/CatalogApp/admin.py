from django.contrib import admin
from CatalogApp.models import Categories, Products, Countries

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'category', 'country']
    search_fields = ['name', 'description']
    list_filter = ['quantity', 'category', 'country', 'nutritional_value', 'cost']

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}