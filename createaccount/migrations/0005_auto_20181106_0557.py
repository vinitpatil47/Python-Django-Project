# Generated by Django 2.0.4 on 2018-11-06 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createaccount', '0004_account_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 5, 57, 6, 122401)),
        ),
    ]
