from .models import Classrooms
from django.contrib import admin


@admin.register(Classrooms)
class ClassroomsAdmin(admin.ModelAdmin):
    list_display = ('id_classroom', 'classroom_title', 'classroom_pops', 'cur_teacher', 'cur_groups')
