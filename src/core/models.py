from django.db import models


class Resource(models.Model):
    """Resource model"""
    title = models.CharField('Название', max_length=255)
    amount = models.FloatField('Количество')
    unit = models.CharField('Единица измерения', max_length=50)
    price = models.FloatField('Цена')
    date = models.DateField('Дата последнего поступления')
