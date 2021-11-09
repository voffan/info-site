from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import CharField, ForeignKey, IntegerField, BooleanField, DecimalField, FloatField, DateTimeField
from django.db.models import Model, CASCADE, SET_NULL


# Create your models here.

class Org(Model):
    name = CharField(verbose_name='Наименование предприятия', max_length=300)
    short_name = CharField(verbose_name='Краткое наименование', max_length=50)
    address = CharField(verbose_name='Юридический адрес', max_length=200)
    telephone = CharField('Номер телефона', max_length=15)
    email = CharField('Адрес э/почты', max_length=100)
    insta = CharField('Ссылка на Instagram аккаунт', max_length=250)
    rss = CharField('Ссылка на RSS', max_length=200)

    def __str__(self):
        return self.short_name


class News(Model):
    title = CharField('Наименование', max_length=300)
    link = CharField('Ссылка', max_length=300, db_index=True)
    pubDate = DateTimeField('Дата публикации')

    def __str__(self):
        return self.title


class Release(Model):
    program = ForeignKey('Program', verbose_name='Программа', on_delete=CASCADE)
    version = CharField('Версия', max_length=20)
    release_date = DateTimeField('Дата релиза')
    link = CharField('Ссылка', max_length=300)
    active = BooleanField('Активная', default=True)

    def __str__(self):
        return self.program.name + ' ' + self.version

    '''def save(self, *args, **kwargs):
        active_release = Release.objects.filter(program__id=self.program.id, active=True).first()
        if active_release is not None:
            active_release.active = False
            active_release.save()
        super().save(*args, **kwargs)
    '''


class Program(Model):
    name = CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name