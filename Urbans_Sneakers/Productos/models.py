from tkinter import CASCADE
from django.db import models
class Category(models.Model):
    category=models.CharField(max_length=40)
    img_category=models.ImageField(null=True, upload_to='img_Category/')
    def __str__(self):
        return self.category

    
class Product(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    model=models.CharField(max_length=40)
    price=models.IntegerField()
    coulor=models.CharField(max_length=40,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    stock=models.IntegerField(null=True)
    img= models.ImageField(null=True, upload_to='img_Product/')
    

