from Productos.models import Category,Sub_Category,Product


def id_category(request):
    id_category=Category.objects.all()
   
    return{
        'id_category':id_category,
    }
def id_sub_category(request):
    id_sub_category=Sub_Category.objects.all()
    
    return{
        'id_sub_category':id_sub_category,
        
    }
def id_product(request):
    id_product=Product.objects.all()
    
    return{
        'id_product':id_product,
        
    }