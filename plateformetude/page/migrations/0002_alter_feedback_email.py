# Generated by Django 5.0.1 on 2024-02-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default='Anonyme', max_length=254),
        ),
    ]
