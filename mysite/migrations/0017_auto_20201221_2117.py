# Generated by Django 3.1.4 on 2020-12-21 21:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20201221_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 21, 17, 50, 239619, tzinfo=utc)),
        ),
    ]