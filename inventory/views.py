from django.shortcuts import redirect, render

from inventory.models import Product
from inventory.forms import ProductForm
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm()
    
    return render(request, 'inventory/add_product.html', {'form': form})