from audioop import reverse
from django.db import models

# Create your models here.

class Column(models.Model):
    title = models.CharField('Название', max_length=50)
    #cards = models.Model('Карточки')

    def __str__(self):
        return self.title

class Card(models.Model):
    text = models.TextField('Карточка', max_length=250)
    #columnName = models.ForeignKey("Column", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Cardss(models.Model):
    text = models.TextField('Карточка', max_length=250)
    #columnName = models.ForeignKey("Column", on_delete=models.CASCADE)
    num = models.IntegerField('Номер_колонки')
    ONE = 'ON'
    TWO = 'TW'
    THREE = 'TH'
    COLUMN_CHOICES = [
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
    ]

    column_choices = models.IntegerField(
        choices = COLUMN_CHOICES,
        default = ONE
    )


class Elemet(models.Model):
    text = models.TextField('Карточка', max_length=250)
    num = models.IntegerField('Номер_колонки', default=1)
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return "/update/%i" % self.id