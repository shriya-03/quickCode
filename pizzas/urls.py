from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index page with the list of pizzas
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),  # Pizza detail page
    path('create/', views.create_pizza, name='create_pizza'),  # Create new pizza page
]
