# Generated by Django 4.0.6 on 2022-08-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0012_alter_product_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]