from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzas/index.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    return render(request, 'pizzas/pizza_detail.html', {'pizza': pizza})
    
    
    
