# Generated by Django 4.0.6 on 2022-08-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_profile_imageee_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='adrres',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
