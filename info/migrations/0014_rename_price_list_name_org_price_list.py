# Generated by Django 3.2.7 on 2021-11-10 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_alter_org_price_list_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='org',
            old_name='price_list_name',
            new_name='price_list',
        ),
    ]
