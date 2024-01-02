from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', views.custom_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

]