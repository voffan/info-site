from django.contrib.auth.models import User
from django.db import transaction
from django.core.validators import validate_email, RegexValidator
from django.db.models import CharField, ForeignKey, ImageField, BooleanField, FileField, FloatField, DateTimeField
from django.db.models import Model, CASCADE, SET_NULL
from info.validators import validate_file_extension


# Create your models here.

phone_validator = RegexValidator(regex=r'^(\+7|8)9\d{9}$|^\d{6}$', message="Номер телефона должен быть введен в формате: +71234567890 или 81234567890 или 123456")

class Org(Model):
    name = CharField(verbose_name='Наименование предприятия', max_length=300)
    short_name = CharField(verbose_name='Краткое наименование', max_length=50)
    address = CharField(verbose_name='Юридический адрес', max_length=200)
    telephone = CharField('Номер телефона', max_length=15, validators=[phone_validator])
    email = CharField('Адрес э/почты', max_length=100, validators=[validate_email])
    insta = CharField('Ссылка на Instagram аккаунт', max_length=250)
    rss = CharField('Ссылка на RSS', max_length=200)
    price_list = FileField(upload_to='pricelists/%m-%Y')

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

    def save(self, recursive_save=True, *args, **kwargs):
        active_release = Release.objects.filter(program__id=self.program.id, active=True).first()
        if active_release is not None and recursive_save:
            active_release.active = False
            active_release.save(recursive_save=False)
        super().save(*args, **kwargs)


class Program(Model):
    name = CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name


class CarouselImage(Model):
    image = FileField(upload_to='images/', validators=[validate_file_extension])
    link = CharField('Ссылка', max_length=300)
    active = BooleanField('Включить в карусель', default=True)

    def __str__(self):
        return self.image.name


class Order(Model):
    name = CharField('Имя', max_length=200)
    email = CharField('Почта', max_length=200, validators=[validate_email])
    phone = CharField('Номер телефона', max_length=15, validators=[phone_validator])
    description = CharField('Описание задачи', max_length=400)
    reg_date = DateTimeField('Дата регистрации', auto_now_add=True)
    is_processed = BooleanField('Обработана', default=False)

    def __str__(self):
        return self.name + ' тел.: ' + self.phone
