# Generated by Django 4.0.6 on 2022-08-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='image',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='imageee',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
