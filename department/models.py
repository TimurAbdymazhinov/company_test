from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Название'
    )

    def __str__(self):
        return self.name if self.name else 'Пустое название'
