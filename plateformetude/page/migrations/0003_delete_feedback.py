# Generated by Django 5.0.1 on 2024-02-11 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_feedback_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
