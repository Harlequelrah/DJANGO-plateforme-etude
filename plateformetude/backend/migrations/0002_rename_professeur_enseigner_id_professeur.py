# Generated by Django 5.0.1 on 2024-02-11 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enseigner',
            old_name='professeur',
            new_name='id_professeur',
        ),
    ]