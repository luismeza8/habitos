# Generated by Django 5.1.3 on 2024-11-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habito_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='dia',
            name='realizado',
            field=models.BooleanField(default=False),
        ),
    ]
