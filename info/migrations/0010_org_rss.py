# Generated by Django 3.2.7 on 2021-11-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_alter_news_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='rss',
            field=models.CharField(default='', max_length=200, verbose_name='Ссылка на RSS'),
            preserve_default=False,
        ),
    ]
