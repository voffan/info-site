# Generated by Django 3.2.7 on 2021-11-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_rename_releases_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='link',
            field=models.CharField(default='', max_length=300, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]