# Generated by Django 5.0 on 2024-01-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0003_alter_coursecontent_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontent',
            name='quiz',
            field=models.FileField(blank=True, upload_to='quiz'),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='file',
            field=models.FileField(upload_to='content/'),
        ),
    ]