# Generated by Django 3.2.7 on 2021-12-23 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20211221_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=200, validators=[django.core.validators.EmailValidator()], verbose_name='Почта'),
        ),
    ]
