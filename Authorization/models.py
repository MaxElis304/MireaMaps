from django import forms
from django.db import models, connection
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission


class UserManager(BaseUserManager):
    def create_user(self, username, user_group, password=None, **extra_fields):
        if not username:
            raise ValueError('The given user_name must be set')
        user = self.model(username=username, user_group=user_group, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, user_group="admin_gr", **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, user_group, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    user_group = models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    class Meta:
        managed = False
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} {self.user_group}'

# with connection.cursor() as cursor:
##      query = "CREATE DEFINER = CURRENT_USER TRIGGER `mireamap`.`authorization_user_AFTER_INSERT` AFTER INSERT ON `authorization_user` FOR EACH ROW BEGIN UPDATE counters SET users_counter = (users_counter + 1); END;"
#     cursor.execute(query)


# with connection.cursor() as cursor:
#     query = "CREATE DEFINER = CURRENT_USER TRIGGER `mireamap`.`authorization_user_AFTER_DELETE` AFTER DELETE ON `authorization_user` FOR EACH ROW BEGIN UPDATE counters SET users_counter = (users_counter - 1); END;"
#     cursor.execute(query)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'user_group', 'password', 'password2')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
