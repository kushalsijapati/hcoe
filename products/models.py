from django.db import models

# Create your models here.
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    Category= models.ForeignKey(Category, on_delete= models.CASCADE)
    price =models.DecimalField(max_digits=10, decimal_places=2) #(10,2)
    description = models.TextField()
    rating = models.IntegerField(default=5)
    
    def __str__(self):
        return self.name
    
    

