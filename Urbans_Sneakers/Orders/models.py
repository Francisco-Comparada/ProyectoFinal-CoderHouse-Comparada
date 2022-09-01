from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from Productos.models import Product
from django.db.models import F,Sum, FloatField

User=get_user_model()



class Order(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_id=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property

    def total(self):
        return self.orders_line_set.aggregate(
            total=Sum(F('price')*F('cant'),out_field=FloatField)
        )['total']
    
    
    class Meta:
        db_table='orders'
        verbose_name='order'
        verbose_name_plural='orders'
        ordering=['id']




class Order_line (models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    cant=models.IntegerField(default=1)
    created_id=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'str{self.cant} units of {self.product.model}'

    class Meta:
            db_table='orders_line'
            verbose_name='Order_line'
            verbose_name_plural='Orders_line'
            ordering=['id']
