# Generated by Django 2.2 on 2020-02-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTaxiDriver', '0005_driver_countrycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='BankAccountDetails',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='driver',
            name='comisionTpv',
            field=models.TextField(default=''),
        ),
    ]