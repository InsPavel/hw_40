from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, null=False, blank=False, default='new', verbose_name='Готовность')

    def __str__(self):
        return f'{self.pk}. {self.name} ({self.status})'
