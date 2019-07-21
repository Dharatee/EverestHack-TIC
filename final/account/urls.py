from django .urls import path
from . import views
from django.conf import settings
from django.contrib.auth import logout

urlpatterns= [
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name= 'logout')
]