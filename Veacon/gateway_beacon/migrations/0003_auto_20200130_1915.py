# Generated by Django 2.2.7 on 2020-01-30 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway_beacon', '0002_gatewaybeaconmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatewaybeaconmodel',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
