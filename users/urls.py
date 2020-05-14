from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name="password_reset"),

]
