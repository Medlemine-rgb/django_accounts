# Generated by Django 3.2.14 on 2022-07-19 19:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(default=datetime.datetime(2022, 7, 19, 19, 56, 57, 803186, tzinfo=utc), upload_to='profile_img'),
            preserve_default=False,
        ),
    ]
