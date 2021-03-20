# Generated by Django 3.1.6 on 2021-03-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0018_auto_20210301_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='address',
        ),
        migrations.RemoveField(
            model_name='application',
            name='name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='status_list',
        ),
        migrations.RemoveField(
            model_name='application',
            name='tests',
        ),
        migrations.AlterField(
            model_name='customer',
            name='afm',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]