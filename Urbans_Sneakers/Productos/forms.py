from django import forms
from .models import Category

class Formulario_Product(forms.Form):
    category=forms.ModelChoiceField(label='Categoria', queryset=Category.objects.all())
    model=forms.CharField(max_length=40)
    price=forms.IntegerField()
    coulor=forms.CharField(max_length=40,required=False)
    description=forms.CharField(max_length=400)
    stock=forms.IntegerField()
    img= forms.ImageField()