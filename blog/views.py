from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.


def blog_page(request):
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
    }
    template_name = 'blog/main.html'

    return render(request, template_name, context)


def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post,
    }
    template_name = 'blog/post.html'

    return render(request, template_name, context)
