
from django.contrib import admin
from django.urls import path,include
from Urbans_Sneakers.views import index,shop
# para las imganes url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('shop/',shop),

     path('Productos/', include('Productos.urls')),#incluye todas las url que estan en sneakers
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)