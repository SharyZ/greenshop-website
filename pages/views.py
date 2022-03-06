from django.shortcuts import render
from django.db.models import Count

from products.models import Category, Product
from blog.models import Post

# Create your views here.


def home_page(request):
    categories = Category.objects.all().annotate(products_count=Count('product'))
    products = Product.objects.order_by('-created_at')
    posts = Post.objects.order_by('-created_at')[:4]

    context = {
        'categories': categories,
        'products': products,
        'posts': posts,
    }
    template_name = 'pages/home.html'

    return render(request, template_name, context)
