from django.db import models
from django.contrib.auth.models import User


class TimeAbstract(models.Model):
    
    created_at = models.DateField('created', auto_now_add=True)
    updated_at = models.DateField('', auto_now=True)
    
    class Meta:
        abstract = True

class Status(TimeAbstract):
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    name = models.CharField(
        max_length=50,
        verbose_name="Название статуса"
    )

    def __str__(self):
        return self.name


class Task(TimeAbstract):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Пользователь"
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Статус"
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Название задачи"
    )

    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )

    deadline = models.DateField(
        verbose_name="Дедлайн",
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="tasks/images/",
        verbose_name="Изображение",
        null=True,
        blank=True
    )

    file = models.FileField(
        upload_to="tasks/files/",
        verbose_name="Файл",
        null=True,
        blank=True
    )


    def __str__(self):
        return self.title


         


# Create your models here.
