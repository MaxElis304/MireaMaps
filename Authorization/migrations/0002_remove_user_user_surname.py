# Generated by Django 4.2.7 on 2023-12-04 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_surname',
        ),
    ]
