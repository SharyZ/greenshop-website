from datetime import datetime

from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name='Name of category', unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    featured_image = models.ImageField(upload_to='products/')
    short_description = models.TextField()
    full_description = RichTextUploadingField(config_name='greenshop_ckeditor')
    in_stock = models.BooleanField(default=True)
    category = models.OneToOneField(
        Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
