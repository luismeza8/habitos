# Generated by Django 5.1.3 on 2024-11-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_dia_realizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='habito',
            name='creacion',
            field=models.DateField(auto_now=True),
        ),
    ]
