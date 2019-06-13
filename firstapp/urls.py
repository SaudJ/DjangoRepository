from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:user_id>', views.profile, name='user-profile'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
]
