  
from django.urls import path
from django.contrib.auth import views as AuthViews
from .views import UsersView

urlpatterns = [
    path('register/', UsersView.register, name='register'),
    path('profile/', UsersView.profile, name='profile'),
    path('login/', AuthViews.LoginView.as_view(template_name='users/login.html'),
            name='login'),
    path('logout/', AuthViews.LogoutView.as_view(template_name='users/logout.html'), 
            name='logout'),
]