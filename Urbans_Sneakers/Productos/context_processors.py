from Productos.models import Category

def id_category(request):
    id_category=Category.objects.all()
    cont=int(3)
    return{
        'id_category':id_category,
        'cont':cont
    }