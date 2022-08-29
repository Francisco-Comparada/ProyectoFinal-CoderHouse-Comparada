from .models import Start_Banner,Featured_Products

def id_banner(request):
    id_banner=Start_Banner.objects.all()
   
    return{
        'id_banner':id_banner,
    }

def id_featured_products(request):
    id_featured_products=Featured_Products.objects.all()
   
    return{
        'id_featured_products':id_featured_products,
    }