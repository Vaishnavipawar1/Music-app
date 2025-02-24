from django.contrib import admin
from django.urls import include, path
from database import views

app_name = 'database'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    

]