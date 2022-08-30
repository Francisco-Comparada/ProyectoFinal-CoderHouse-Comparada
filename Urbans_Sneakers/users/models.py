from django.db import models

class User_profile(models.Model):
    first_name = models.CharField(max_length=150,blank=True)
    last_name = models.CharField(max_length=150,blank=True)
    user=models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name='profile')
    phone=models.CharField(max_length=25,blank=True)
    address=models.CharField(max_length=150,blank=True)
    image=models.ImageField(upload_to='profile_image',blank=True)

