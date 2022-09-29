# Generated by Django 4.1 on 2022-09-23 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=13)),
                ('tipo', models.CharField(choices=[('C', 'Casa'), ('M', 'Celular'), ('T', 'Trabajo')], default='C', max_length=1)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
            ],
        ),
    ]
