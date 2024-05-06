from django.db import models


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=1, max_digits=4)
    country = models.CharField(max_length=40)
    nutritional_value = models.DecimalField(decimal_places=2, max_digits=5)
    manufactures = models.CharField(max_length=40)
    category = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"