# Generated by Django 5.0.1 on 2024-02-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_feedback_email_feedback_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='id_Session',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
