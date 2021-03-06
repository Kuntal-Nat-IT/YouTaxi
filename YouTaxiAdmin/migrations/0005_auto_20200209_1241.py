# Generated by Django 2.2 on 2020-02-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTaxiAdmin', '0004_car_zipcodeworkcity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='addDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='buyDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='lastITVdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='lastMetropolitandate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='lastVerificationdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='registrationDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='removeDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
