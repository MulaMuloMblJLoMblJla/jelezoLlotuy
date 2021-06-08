from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    request_type = [
        ('1', 'One'),
        ('2', 'Two'),
    ]
    name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Email', max_length=100)
    request = models.CharField('Запрос', max_length=100, choices=request_type)
    text = models.TextField('Текст')

    def __str__(self):
        return self.name + self.last_name

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


class SubMenu(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'
