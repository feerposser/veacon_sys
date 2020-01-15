# Generated by Django 2.2.7 on 2020-01-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_veacon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaque', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(to='user_veacon.UserVeaconModel')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
    ]
