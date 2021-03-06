# Generated by Django 2.0.4 on 2018-11-06 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createaccount', '0009_auto_20181106_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_status',
            field=models.CharField(default='Saving', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(default='Saving', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='email_id',
            field=models.EmailField(default='none', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(default='NN', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='mobile_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='occupation',
            field=models.CharField(default='NA', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='qualification',
            field=models.CharField(default='NA', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2018, 11, 6, 7, 12, 15, 115017)),
        ),
    ]
