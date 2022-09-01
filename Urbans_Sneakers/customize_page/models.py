from django.db import models


    
class Start_Banner(models.Model):
    banner=models.CharField(max_length=20)
    title_banner=models.CharField(max_length=150)
    sub_tittle_banner=models.CharField(max_length=250)
    text_banner=models.CharField(max_length=500)
    img_banner=models.ImageField(upload_to='banner_img')
    def __str__(self):
        return self.banner



class Featured_Products(models.Model):
   
    product=models.CharField(max_length=40)
