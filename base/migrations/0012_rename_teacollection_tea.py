# Generated by Django 4.2.7 on 2023-11-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_quantity_teacollection_farmer_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeaCollection',
            new_name='Tea',
        ),
    ]
