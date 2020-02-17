# Generated by Django 2.2 on 2020-02-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTaxiAdmin', '0009_paymenthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='RideHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phoneNo', models.TextField()),
                ('startPoint', models.TextField()),
                ('endPoint', models.TextField()),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]
