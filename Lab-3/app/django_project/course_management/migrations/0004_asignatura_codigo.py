# Generated by Django 3.2.3 on 2023-09-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0003_alumno_asignaturas'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='codigo',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
