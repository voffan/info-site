# Generated by Django 3.2.7 on 2021-11-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_release_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(db_index=True, max_length=300, verbose_name='Ссылка'),
        ),
    ]
