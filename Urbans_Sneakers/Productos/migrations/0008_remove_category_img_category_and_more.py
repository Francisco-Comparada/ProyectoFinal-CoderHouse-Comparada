# Generated by Django 4.0.6 on 2022-08-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0007_sub_category_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='img_category',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='img_sub_category',
            field=models.ImageField(null=True, upload_to='img_sub_Category/'),
        ),
    ]
