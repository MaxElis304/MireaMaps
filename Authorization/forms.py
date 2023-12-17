from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'user_group', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

    def get_user(self):
        return super().get_user()


