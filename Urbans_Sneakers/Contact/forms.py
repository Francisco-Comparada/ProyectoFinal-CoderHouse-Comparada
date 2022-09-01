from django import forms

class form_contact(forms.Form):
    name=forms.CharField(label='Name', required= True)    
    email=forms.CharField(label='Email', required= True)
    subject=forms.CharField(label='subject', required=True)
    message=forms.CharField(label='Message', required=True)