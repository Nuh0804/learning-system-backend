# Generated by Django 5.0 on 2023-12-25 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0002_rename_problem_question_question_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='correct_answer',
            new_name='is_correct',
        ),
    ]