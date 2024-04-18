from django.db import models


class RegisteredUsers(models.Model):
    name = models.CharField('Имя', max_length=50, default='')
    surname = models.CharField('Фамилия', max_length=50, default='')
    email = models.CharField('Электронная почта', max_length=50, default='')
    password = models.CharField('Пароль', max_length=50, default='')
    password_check = models.CharField('Повторить пароль', max_length=50, default='')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

