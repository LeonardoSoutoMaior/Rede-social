# Generated by Django 5.0.3 on 2024-03-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='total_seguindo',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
