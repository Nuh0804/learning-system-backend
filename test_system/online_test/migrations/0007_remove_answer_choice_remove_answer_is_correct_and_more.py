# Generated by Django 5.0 on 2023-12-26 05:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0006_alter_question_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='value',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='answer',
            name='marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='online_test.question'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1)),
                ('choice', models.CharField(max_length=50)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='online_test.question')),
            ],
        ),
    ]
