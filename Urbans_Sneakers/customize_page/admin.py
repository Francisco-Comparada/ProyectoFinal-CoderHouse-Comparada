from django.contrib import admin

from .models import Start_Banner,Featured_Products
# Register your models here.
      
@admin.register(Start_Banner)
class Start_Banner_admin(admin.ModelAdmin):
    list_display = ['banner','title_banner','sub_tittle_banner','text_banner','img_banner']                    