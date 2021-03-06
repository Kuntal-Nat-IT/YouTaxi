# Generated by Django 2.2 on 2020-01-30 07:49

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('phoneNo', models.TextField()),
                ('address', models.TextField()),
                ('role', models.TextField(default='subAdmin')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resetPasswordToken', models.TextField(default='token')),
                ('tokenExpiration', models.BigIntegerField(default='10101')),
            ],
        ),
        migrations.CreateModel(
            name='CMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('pageName', models.TextField()),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default='False')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('baseFare', models.FloatField()),
                ('vehicleTypeId', models.TextField()),
                ('fromTime', models.TimeField(auto_now_add=True)),
                ('toTime', models.TimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypalEmail', models.EmailField(max_length=254)),
                ('siteEmail', models.EmailField(max_length=254)),
                ('mobile', models.TextField()),
                ('skype', models.TextField()),
                ('siteName', models.TextField()),
                ('address', models.TextField()),
                ('iconFile', models.ImageField(default='default/Image/avater.jpeg', upload_to='Admin/Setting/Icon/')),
                ('logoFile', models.ImageField(default='default/Image/avater.jpeg', upload_to='Admin/Setting/Logo/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('baseTripNo', models.IntegerField()),
                ('baseAmountReceivable', models.FloatField()),
                ('bonusTripNo', models.IntegerField()),
                ('bonusAmountReceivable', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrationNo', models.TextField()),
                ('manufactureYear', models.TextField()),
                ('state', models.TextField()),
                ('color', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleType', models.TextField(default='')),
                ('driverId', models.TextField()),
                ('AddDate', models.DateTimeField(auto_now_add=True)),
                ('BuyDate', models.DateTimeField(auto_now_add=True)),
                ('RegistrationDate', models.DateTimeField(auto_now_add=True)),
                ('LastITVDate', models.DateTimeField(auto_now_add=True)),
                ('LastMetroDate', models.DateTimeField(auto_now_add=True)),
                ('ServicesToPerform', djongo.models.fields.ListField(default=[])),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('baseFare', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
