from django.core.validators import MinLengthValidator
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)], blank=False, null=False,
                            verbose_name="Название задания")
    start_datetime = models.DateTimeField(null=False, blank=False,
                                          verbose_name="Дата/время начала")
    execution_length_datetime = models.DateTimeField(null=False, blank=False,
                                                     verbose_name="Длина выполнения (дата/время)")
    is_canceled = models.BooleanField(null=False, default=False, blank=False,
                                      verbose_name="Отменено")
