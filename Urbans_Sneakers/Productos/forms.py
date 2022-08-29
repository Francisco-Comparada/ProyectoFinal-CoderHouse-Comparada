from tkinter import Widget
from tkinter.tix import Select
from django import forms
from .models import Category, Sub_Category

class Formulario_Create_Category(forms.Form):
    category=forms.CharField(max_length=75)

class Formulario_Create_Sub_Category(forms.Form):
    category=forms.ModelChoiceField(label='Categoria', queryset=Category.objects.all())
    sub_category=forms.CharField(max_length=75)
    img_sub_category= forms.ImageField(required=False)

class Formulario_Product(forms.Form):
    category=forms.ModelChoiceField(label='Categoria', queryset=Category.objects.all())
    sub_category=forms.ModelChoiceField(label='Sub-Categoria', queryset=Sub_Category.objects.all())
    model=forms.CharField(max_length=40)
    price=forms.FloatField()
    coulor=forms.CharField(max_length=40,required=False)
    description=forms.CharField(max_length=400)
    stock=forms.IntegerField()
    img= forms.ImageField(required=False)

