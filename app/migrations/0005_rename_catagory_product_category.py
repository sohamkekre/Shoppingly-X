# Generated by Django 4.1.7 on 2023-04-16 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_customer_orderplaced_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
    ]
