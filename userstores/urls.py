from django.contrib import admin
from django.urls import path, include
from .views  import allstores, userprofile, storedetail
from django.contrib.auth.views import PasswordResetView
from .views import login_view, logout_view, register_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', allstores, name='home'),
    path('profile/', userprofile, name='userprofile'),
    path('<str:slug>/', storedetail, name='storedetail')
        
]
