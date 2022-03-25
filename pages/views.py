from django.shortcuts import render
from django.db.models import Count

from products.models import Category, Product
from blog.models import Post

# Create your views here.


def home_page(request):
    if 'cat' in request.GET:
        cat = request.GET['cat']
        products = Product.objects.filter(category__id=cat)
    else:
        products = Product.objects.order_by('-created_at')

    categories = Category.objects.all().annotate(products_count=Count('product'))
    products_count = products.count()
    posts = Post.objects.order_by('-created_at')[:4]

    context = {
        'categories': categories,
        'products': products,
        'products_count': products_count,
        'posts': posts,
    }
    template_name = 'pages/home.html'

    return render(request, template_name, context)
