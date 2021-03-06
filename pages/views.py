from django.shortcuts import render
from django.db.models import Count

from products.models import Category, Product
from blog.models import Post

# Create your views here.


def home_page(request):
    categories = Category.objects.all().annotate(products_count=Count('product'))
    products = Product.objects.order_by('-created_at')[:6]

    active_category = int(request.GET.get('cat', 0))

    if active_category:
        products = Product.objects.filter(
            category__id=active_category).order_by('-created_at')[:6]

    products_count = products.count()
    posts = Post.objects.order_by('-created_at')[:4]

    context = {
        'categories': categories,
        'active_category': active_category,
        'products': products,
        'products_count': products_count,
        'posts': posts,
    }
    template_name = 'pages/home.html'

    return render(request, template_name, context)
