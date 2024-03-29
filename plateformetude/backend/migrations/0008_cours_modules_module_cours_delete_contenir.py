# Generated by Django 5.0.1 on 2024-03-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_id_cours_enseigner_cours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='modules',
            field=models.ManyToManyField(related_name='modules_cours', to='backend.module'),
        ),
        migrations.AddField(
            model_name='module',
            name='cours',
            field=models.ManyToManyField(related_name='cours_modules', to='backend.cours'),
        ),
        migrations.DeleteModel(
            name='Contenir',
        ),
    ]
