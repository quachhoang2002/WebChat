from turtle import home
from unicodedata import name
from django.urls import path 
from . import views 
app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('room/<str:pk>',views.room,name='room'),
    path('create_room/',views.createRoom,name='create_room'),
    path('update_room/<str:pk>',views.updateRoom,name='update_room'),
    path('delete/<str:pk>',views.delelteRoom,name='delete_room'),
    path("registerForm/",views.registerUser, name="register_user"),
    path("loginForm/",views.Login, name="login_form"),
    path("logout/",views.Logout,name='logout'),

]



