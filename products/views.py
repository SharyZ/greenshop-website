from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage

from .models import Category, Product

# Create your views here.


def products_page(request):
    categories = Category.objects.all().annotate(products_count=Count('product'))
    products = Product.objects.order_by('-created_at')

    active_category = int(request.GET.get('cat', 0))

    if active_category:
        products = Product.objects.filter(
            category__id=active_category).order_by('-created_at')

    products_count = products.count()

    products = Paginator(products, 6)
    page_number = request.GET.get('page', 1)

    try:
        products = products.page(page_number)
    except EmptyPage:
        products = products.page(1)

    context = {
        'categories': categories,
        'active_category': active_category,
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
