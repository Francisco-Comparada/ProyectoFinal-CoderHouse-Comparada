
from django.contrib import admin
from django.urls import path,include
from Urbans_Sneakers.views import index,shop,setting,base,customize_page,about 
# para las imganes url
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),

    path('',index),
    path('shop/',shop),
    path('setting/',setting),
    path('base/',base),
    path('about/',about),
    path('customize_page/',customize_page),


    path('users/', include('users.urls')),
    path('Productos/', include('Productos.urls')),
    path('Cart/', include('Cart.urls')),
    path('customize_page/', include('customize_page.urls')),
    path('Orders/', include('Orders.urls')),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)