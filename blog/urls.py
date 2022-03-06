from django.urls import path

from .views import blog_page, post_page


urlpatterns = [
    path('', blog_page, name='blog'),
    path('<int:post_id>/', post_page, name='post'),
]
