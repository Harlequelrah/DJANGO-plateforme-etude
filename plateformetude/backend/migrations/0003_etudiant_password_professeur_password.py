# Generated by Django 5.0.1 on 2024-02-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_professeur_enseigner_id_professeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
