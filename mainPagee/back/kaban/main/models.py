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



