# urls.py в приложении Authorization
from django.urls import path
from .views import register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
