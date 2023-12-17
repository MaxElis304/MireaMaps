from django.db import models, connection


class Classrooms(models.Model):
    id_classroom = models.AutoField(primary_key=True)
    classroom_title = models.CharField(max_length=45)
    classroom_pops = models.CharField(max_length=45)
    cur_teacher = models.CharField(max_length=45, blank=True, null=True)
    cur_groups = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classrooms'
        verbose_name = 'Аудитории'
        verbose_name_plural = 'Аудитории'

    def __str__(self):
        return f"{self.classroom_title} (ID: {self.id_classroom})"

