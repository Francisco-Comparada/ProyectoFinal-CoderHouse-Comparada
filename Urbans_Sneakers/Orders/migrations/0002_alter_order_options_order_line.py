# Generated by Django 4.0.6 on 2022-08-25 18:47

import builtins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0012_alter_product_img_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': [builtins.id], 'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.CreateModel(
            name='Order_line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=1)),
                ('created_id', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order_line',
                'verbose_name_plural': 'Orders_line',
                'db_table': 'orders_line',
                'ordering': [builtins.id],
            },
        ),
    ]
