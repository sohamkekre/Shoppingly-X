# Generated by Django 4.1.7 on 2023-04-14 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_prodect_image_product_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Product',
            new_name='product',
        ),
    ]
