from django.urls import path
from .import views


urlpatterns = [
   # path('',views.product_list,name='products_list'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    ]