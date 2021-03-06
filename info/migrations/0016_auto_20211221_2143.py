# Generated by Django 3.2.7 on 2021-12-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_carouselimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('email', models.CharField(max_length=200, verbose_name='Почта')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('description', models.CharField(max_length=400, verbose_name='Описание задачи')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Обработана')),
            ],
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Включить в карусель'),
        ),
    ]
