# Generated by Django 4.2.7 on 2023-11-18 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_f_contact_teacollection_farmer_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacollection',
            old_name='amount',
            new_name='Amount',
        ),
        migrations.RenameField(
            model_name='teacollection',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='teacollection',
            old_name='paid',
            new_name='Paid',
        ),
        migrations.RenameField(
            model_name='teacollection',
            old_name='quantity',
            new_name='Quantity',
        ),
    ]
