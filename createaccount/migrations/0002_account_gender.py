# Generated by Django 2.0.4 on 2018-11-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createaccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(default='male', max_length=2),
        ),
    ]
