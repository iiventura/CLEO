# Generated by Django 2.1.2 on 2019-02-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('dni', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.EmailField(blank=True, max_length=45, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('password', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'Empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoempleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipoEmpleado',
                'managed': False,
            },
        ),
    ]
