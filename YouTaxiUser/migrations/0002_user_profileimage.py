# Generated by Django 2.2 on 2020-01-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTaxiUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ProfileImage',
            field=models.ImageField(default='default/Image/avater.jpeg', upload_to='User/ProfileImage/'),
        ),
    ]
