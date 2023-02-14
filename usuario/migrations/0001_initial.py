# Generated by Django 4.1.6 on 2023-02-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='apellidos')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil', verbose_name='foto de perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
