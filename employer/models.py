from django.db import models

from common.utils import generate_filename
from department.models import Department


class Employer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=50, null=True, blank=True, verbose_name='Фвмилия', db_index=True)

    avatar = models.ImageField(upload_to=generate_filename, null=True, blank=True, verbose_name='Фото')
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name='Должность')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Оклад')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Возраст')
    department = models.ForeignKey(
        to=Department, on_delete=models.SET_NULL, verbose_name='Департамент', related_name='employers', null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Cотрудник'
        verbose_name_plural = 'Cотрудники'

    def __str__(self):
        return f'{self.name}'

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'
