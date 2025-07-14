from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from django.contrib.auth import views as auth_views

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('password/', auth_views.PasswordResetView.as_view(
        template_name='mail/password-reset.html',
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='mail/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='mail/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='mail/password_reset_complete.html'), name='password_reset_complete')
]
