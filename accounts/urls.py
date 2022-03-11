from django.urls import path
from .views import cart_page, logout_page, profile_page, login_page, signup_page


urlpatterns = [
    path('profile/', profile_page, name='profile'),
    path('cart/', cart_page, name='cart'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('logout/', logout_page, name='logout'),
]
