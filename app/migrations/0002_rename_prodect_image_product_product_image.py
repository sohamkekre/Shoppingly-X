# Generated by Django 4.1.7 on 2023-04-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prodect_image',
            new_name='product_image',
        ),
    ]
