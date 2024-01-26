# Generated by Django 5.0 on 2024-01-26 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0010_courseforteacher_course_student_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_system.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_system.student')),
            ],
        ),
    ]
