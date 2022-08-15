from django import forms

categories=(
    ('Jordans','Jordans'),
    ('Air Force','Air Force'),
    ('Accesorio','Accesorio'),
    )


class Formulario_Product(forms.Form):
    category=forms.ChoiceField(choices=categories)
    model=forms.CharField(max_length=40)
    price=forms.IntegerField()
    coulor=forms.CharField(max_length=40)
    description=forms.CharField(max_length=400)
    stock=forms.IntegerField()
    img= forms.ImageField()