from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import CharField, ForeignKey, IntegerField, BooleanField, DecimalField, FloatField, DateTimeField
from django.db.models import Model, CASCADE, SET_NULL


# Create your models here.

class Org(Model):
    name = CharField(verbose_name='Наименование предприятия', max_length=150)
    address = CharField(verbose_name='Юридический адрес', max_length=200)