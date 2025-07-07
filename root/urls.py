from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
]
