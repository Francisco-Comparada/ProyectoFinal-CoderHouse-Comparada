from email.policy import default
from tkinter import CASCADE
from django.db import models


class Category(models.Model):
    category=models.CharField(max_length=75)
    def __str__(self):
        return self.category

class Sub_Category(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    sub_category=models.CharField(max_length=75)
    img_sub_category=models.ImageField(upload_to='img_sub_Category/',blank=True)
    def __str__(self):
        return self.sub_category


class Product(models.Model):
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    sub_category=models.ForeignKey('Sub_Category',on_delete=models.CASCADE,null=True)
    model=models.CharField(max_length=40)
    price=models.IntegerField()
    coulor=models.CharField(max_length=40,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    stock=models.IntegerField(null=True)
    img= models.ImageField(upload_to='img_Product/',blank=True )
    

