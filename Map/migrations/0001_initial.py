# Generated by Django 4.2.7 on 2023-12-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id_classroom', models.AutoField(primary_key=True, serialize=False)),
                ('classroom_title', models.CharField(max_length=45)),
                ('classroom_pops', models.CharField(max_length=45)),
                ('cur_teacher', models.CharField(blank=True, max_length=45, null=True)),
                ('cur_groups', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'classrooms',
                'managed': False,
            },
        ),
    ]
