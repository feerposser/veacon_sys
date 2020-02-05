# Generated by Django 2.2.7 on 2020-02-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchpost', '0004_auto_20200203_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchpostmodel',
            name='rssi_max',
        ),
        migrations.RemoveField(
            model_name='watchpostmodel',
            name='rssi_min',
        ),
        migrations.AddField(
            model_name='watchpostmodel',
            name='rssi_far',
            field=models.FloatField(blank=True, help_text='RSSI mais distante', null=True, verbose_name='RSSI distante'),
        ),
        migrations.AddField(
            model_name='watchpostmodel',
            name='rssi_near',
            field=models.FloatField(blank=True, help_text='RSSI mais próximo', null=True, verbose_name='RSSI próximo'),
        ),
    ]
