from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

app_name = 'home'

urlpatterns = [

    path('', views.index, name = 'index'),

    path('edu/', views.edu, name = 'edu'),

    path('user/', views.user, name = 'user'),

]