# Generated by Django 3.2.7 on 2021-11-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_org_rss'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активная'),
        ),
    ]
