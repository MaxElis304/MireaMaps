# Generated by Django 4.2.7 on 2023-12-08 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization', '0005_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False, 'verbose_name_plural': 'Пользователи'},
        ),
    ]