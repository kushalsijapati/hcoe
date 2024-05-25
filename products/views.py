from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import ProductSerializer
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html',{'products':products})

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']
    
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer
    
# Create your views here.
