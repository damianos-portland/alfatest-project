# Generated by Django 3.1.6 on 2021-03-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0025_trial_yliko'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='doy',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='fax',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
