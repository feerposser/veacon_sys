# Generated by Django 2.2.7 on 2020-01-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertmodel',
            name='watchpost_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='watchpost.WatchpostModel', verbose_name='Monitoramento'),
        ),
    ]
