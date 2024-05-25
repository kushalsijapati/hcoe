from django.db import models


class Customer (models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=50,default=0)
    address=models.CharField(max_length=100,default=0)
    
    def __str__(self):
        return self.name
    
 