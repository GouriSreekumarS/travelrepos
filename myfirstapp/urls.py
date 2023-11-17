from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [

    path('', views.hello, name='hello'),
    path('register/', views.registration, name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')

]
