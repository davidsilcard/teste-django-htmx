from django.shortcuts import render
from .models import Product

# Create your views here.
def list_products(request):
    return render(request, 'app/list_products.html')

