# Generated by Django 2.0.4 on 2018-11-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createaccount', '0019_auto_20181112_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=11444501871),
        ),
    ]
