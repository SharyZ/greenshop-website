from django.urls import path
from .views import logout_page, profile_edit_page, profile_page, login_page, signup_page


urlpatterns = [
    path('profile/', profile_page, name='profile'),
    path('profile/edit', profile_edit_page, name='profile-edit'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('logout/', logout_page, name='logout'),
]
