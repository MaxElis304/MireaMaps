from django.db import models
from Authorization.models import User


class Counters(models.Model):
    id = models.AutoField(primary_key=True)
    users_counter = models.IntegerField()
    classrooms_counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'counters'
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчики'

    def __str__(self):
        return f"{self.users_counter} {self.classrooms_counter})"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class AuthorizationUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authorization_user_groups'
        unique_together = (('user', 'group'),)
        verbose_name = 'Группа авторизованных пользователей'
        verbose_name_plural = 'Группы авторизованных пользователей'
