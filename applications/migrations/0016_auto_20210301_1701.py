# Generated by Django 3.1.6 on 2021-03-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_auto_20210227_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='protocol_number',
            field=models.IntegerField(unique=True),
        ),
    ]