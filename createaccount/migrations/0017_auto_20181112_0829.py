# Generated by Django 2.0.4 on 2018-11-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createaccount', '0016_auto_20181112_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='j',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=11863569530),
        ),
    ]
