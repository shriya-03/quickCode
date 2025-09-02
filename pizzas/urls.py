from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
     path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
]
