from django.db import models

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name='Имя категории')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    icon = models.ImageField(upload_to='icon_category', verbose_name='Иконка')
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35,verbose_name='Название страны')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'
    def __str__(self):
        return self.name

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='products_images', verbose_name='Фотография')
    description = models.CharField(max_length=200, verbose_name='Описание', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    cost = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Цена')
    nutritional_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=5, verbose_name='Калорийность')
    manufactures = models.CharField(max_length=40, verbose_name='Производитель')
    country = models.ForeignKey(to=Countries, on_delete=models.PROTECT, verbose_name='Страна')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"