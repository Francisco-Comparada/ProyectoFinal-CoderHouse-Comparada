from unicodedata import category
from django.db import models

class Product(models.Model):
    category=models.CharField(max_length=40)
    model=models.CharField(max_length=40)
    price=models.IntegerField()
    coulor=models.CharField(max_length=40,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    stock=models.IntegerField(null=True)
    img= models.ImageField(null=True, upload_to='img_Jordan/')

def __str__(self):
        return self.model