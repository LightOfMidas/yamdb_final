from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_CHOICES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin')
    ]
    username = models.CharField('Пользователь', max_length=50, unique=True)
    email = models.EmailField('Электронная почта', unique=True)
    first_name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    bio = models.TextField('Биография', max_length=200, blank=True)
    role = models.CharField(
        'Статус пользователя',
        choices=ROLE_CHOICES,
        max_length=50,
        default=USER
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('id',)
