# Generated by Django 5.0 on 2023-12-26 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0007_remove_answer_choice_remove_answer_is_correct_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
