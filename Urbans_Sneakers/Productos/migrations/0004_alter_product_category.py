# Generated by Django 4.0.6 on 2022-08-18 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_category_img_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Productos.category'),
        ),
    ]