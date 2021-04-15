from django.db import models


class Resources(models.Model):
    title = models.CharField('Название', max_length=255)
    amount = models.FloatField('Количество')
    unit = models.CharField('Единица измерения', max_length=50)
    price = models.FloatField('Цена')
    date = models.DateTimeField('Дата последнего поступления')
