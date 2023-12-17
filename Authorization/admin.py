from .models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'username', 'user_group', 'is_staff', 'is_superuser', 'password')


