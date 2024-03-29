# Generated by Django 3.2.14 on 2022-07-21 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicament', '0002_auto_20220721_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='img_medical',
            field=models.ImageField(default='medical_img/default.png', upload_to='medical_img/'),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='date_de_prise',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
