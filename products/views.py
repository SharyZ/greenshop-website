from django.shortcuts import get_object_or_404, render
from django.db.models import Count

from .models import Category, Product

# Create your views here.


def products_page(request):
    categories = Category.objects.all().annotate(products_count=Count('product'))
    products = Product.objects.order_by('-created_at')
    products_count = products.count()

    context = {
        'categories': categories,
        'products': products,
        'products_count': products_count,
    }
    template_name = 'products/main.html'

    return render(request, template_name, context)


def product_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }
    template_name = 'products/product.html'

    return render(request, template_name, context)
