# jojo_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_stand, name='upload_stand'),
    path('stands/', views.stand_list, name='stand_list'),
]
