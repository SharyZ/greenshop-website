from django.urls import path

from .views import product_page, products_page


urlpatterns = [
    path('', products_page, name='products'),
    path('<int:product_id>/', product_page, name='product'),
]
