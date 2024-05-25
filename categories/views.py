from django.shortcuts import render
from products.models import Product
from .models import Category

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_products(request):
    categories=Category.objects.all()
    products=Product.objects.all()
    return render(request,'categories/category_products.html', {'categories': categories, 'products': products})