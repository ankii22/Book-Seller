# Generated by Django 2.2.3 on 2019-10-07 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20191007_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='datetime',
            field=models.DateField(default=datetime.date.today),
        ),
    ]