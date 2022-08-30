from django import forms
from Productos.models import Product




n_banner=(
    ('1', 'Pricipal'),
    ('2', 'Secundario'),
)



n_product=(
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)



class Form_start_Banner(forms.Form):
    banner=forms.ChoiceField(label='Numero de banner...',choices=n_banner)
    title_banner=forms.CharField(required=True)
    sub_tittle_banner=forms.CharField(required=False)
    text_banner=forms.CharField(required=True)
    img_banner=forms.ImageField(required=True)



class Form_Featured_Products(forms.Form):
    n_product=forms.ChoiceField(label='Poducto destacado numero...',choices=n_product)
    product=forms.ModelChoiceField(label='Seleccionar producto', queryset=Product.objects.all())