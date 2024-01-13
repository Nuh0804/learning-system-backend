# Generated by Django 5.0 on 2023-12-28 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0011_remove_test_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default='CS151', on_delete=django.db.models.deletion.CASCADE, to='online_test.test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='course',
            field=models.ForeignKey(default='CS151', on_delete=django.db.models.deletion.CASCADE, to='online_test.test'),
            preserve_default=False,
        ),
    ]
