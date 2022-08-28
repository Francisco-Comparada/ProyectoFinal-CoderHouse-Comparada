from django.urls import path
from users.views import login_request,register,edit_profile,create_profile,profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('create_profile/', create_profile, name='create_profile'),
    
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html')),  
]