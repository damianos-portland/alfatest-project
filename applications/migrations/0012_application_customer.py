# Generated by Django 3.1.6 on 2021-02-27 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0011_auto_20210227_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='applications.customer'),
        ),
    ]
