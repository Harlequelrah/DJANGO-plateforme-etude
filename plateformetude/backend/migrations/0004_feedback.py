# Generated by Django 5.0.1 on 2024-02-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_etudiant_password_professeur_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='Anonyme', max_length=254, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
