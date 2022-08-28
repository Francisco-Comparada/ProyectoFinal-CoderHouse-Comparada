from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,AbstractUser
from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
   
  
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:'' for k in fields} # Saca los comentarios de ayuda

class User_edit_form(forms.Form):
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ( 'email', 'password1', 'password2','phone','address','image')
        help_texts = {k:'' for k in fields} # Saca los comentarios de ayuda