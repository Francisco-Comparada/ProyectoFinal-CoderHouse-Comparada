from django import forms



class Formulario_Product(forms.Form):
    category=forms.CharField(max_length=40)
    model=forms.CharField(max_length=40)
    price=forms.IntegerField()
    coulor=forms.CharField(max_length=40,null=True,blank=True)
    description=forms.CharField(max_length=400,null=True,blank=True)
    stock=forms.IntegerField
    img= forms.ImageField()