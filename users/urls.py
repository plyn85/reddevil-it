from django.urls import path
from .views import register, profile, order_history, MyLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', register, name="register"),
    path('login/', MyLoginView.as_view(template_name='users/login.html'),
         name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_comfirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name="password_reset-compelete"),
    path('order_history/<transaction_id>',
         order_history, name='order_history'),

]
