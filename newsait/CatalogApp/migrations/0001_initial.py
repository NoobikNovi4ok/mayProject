# Generated by Django 5.0.4 on 2024-05-11 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Имя категории')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('icon', models.ImageField(upload_to='icon_category', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35, verbose_name='Название страны')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Страну',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='products_images', verbose_name='Фотография')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Цена')),
                ('nutritional_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Калорийность')),
                ('manufactures', models.CharField(max_length=40, verbose_name='Производитель')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CatalogApp.categories', verbose_name='Категория')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CatalogApp.countries', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
