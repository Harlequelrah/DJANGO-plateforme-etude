# Generated by Django 5.0.1 on 2024-02-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.AddField(
            model_name='feedback',
            name='full_name',
            field=models.CharField(default='Anonyme', max_length=50, null=True),
        ),
    ]
