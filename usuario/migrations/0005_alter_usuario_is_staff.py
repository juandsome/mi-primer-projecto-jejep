# Generated by Django 4.1.6 on 2023-02-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_usuario_is_active_usuario_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
