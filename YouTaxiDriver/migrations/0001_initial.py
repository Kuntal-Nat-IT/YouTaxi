# Generated by Django 2.2 on 2020-01-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('phoneNo', models.TextField()),
                ('landLineNumber', models.TextField(default='')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(default='')),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('dateOfBirth', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('removeDate', models.DateTimeField(auto_now_add=True)),
                ('placeOfBirth', models.TextField(default='')),
                ('DNIAddress', models.TextField(default='')),
                ('DNICityAddress', models.TextField(default='')),
                ('ExpirationDateCirculationPermit', models.TextField(default='')),
                ('Regularschedule', models.TextField(default='')),
                ('LinkedTaxiLicense', models.TextField(default='')),
                ('RegistrationTaxiLinked', models.TextField(default='')),
                ('language', models.TextField(default='Spanish')),
                ('TravelCommission', models.TextField(default='')),
                ('CommissionChargeCards', models.TextField(default='')),
                ('BankCurrentAccount', models.TextField(default='')),
                ('AdminNotices', models.TextField(default='')),
                ('AdminNotes', models.TextField(default='')),
                ('driverScore', models.FloatField(default='0.0')),
                ('ImeiCode', models.TextField(default='')),
                ('HashCode', models.TextField(default='')),
                ('profileImg', models.ImageField(default='default/Image/avater.jpeg', upload_to='Driver/DriverProfile/')),
                ('PhotoDNI', models.TextField(default='')),
                ('CredintialPhoto', models.ImageField(default='default/Image/avater.jpeg', upload_to='Driver/Crediantial/')),
                ('location', models.TextField(default='88.23478, 25.36578')),
                ('driverOTP', models.TextField(default='')),
                ('preferedHour', models.TextField(default='AM')),
            ],
        ),
    ]
