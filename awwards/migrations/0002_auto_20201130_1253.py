# Generated by Django 3.1.3 on 2020-11-30 09:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='home',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='photos'),
        ),
    ]
