# Generated by Django 4.0.6 on 2022-08-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0009_alter_product_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='img_Product/default.png', upload_to='img_Product/'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='img_sub_category',
            field=models.ImageField(default='img_sub_Category/default.png', upload_to='img_sub_Category/'),
        ),
    ]
