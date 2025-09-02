# pizzas/views.py
from django.shortcuts import render, redirect
from .models import Pizza
from .forms import PizzaForm

# View to list all pizzas
def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzas/index.html', {'pizzas': pizzas})

# View for pizza detail
def pizza_detail(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    return render(request, 'pizzas/pizza_detail.html', {'pizza': pizza})

# View to create a new pizza
def create_pizza(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        pizza_form = PizzaForm()
    else:
        # POST data submitted; process data.
        pizza_form = PizzaForm(data=request.POST)
        if pizza_form.is_valid():
            pizza_form.save()
            return redirect('index')  # Neeed to redirect to the index page to view the new pizza
    
    context = {'form': pizza_form}
    return render(request, 'pizzas/create_pizza.html', context)
