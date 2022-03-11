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


class Cart(models.Model):
    customer = models.ForeignKey(
        'accounts.Customer', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def get_cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    @property
    def get_cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    @property
    def get_cart_total_with_shiping(self, shiping=16):
        return self.get_cart_total + shiping


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey(
        Cart, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
