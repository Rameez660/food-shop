from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('ordernow/', views.ordernow, name='ordernow'),
    path('blog/', views.blog, name='blog'),
    path('search/',views.search,name='search'),
    path('signup/',views.signup,name='signup'),
    path('register_user/',views.register_user,name='register_user'),
    path('login/',views.login,name='login'),
    path('logout/',views.handlelogout,name='handlelogout')
]