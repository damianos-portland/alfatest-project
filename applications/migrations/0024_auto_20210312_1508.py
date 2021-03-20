# Generated by Django 3.1.6 on 2021-03-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0023_auto_20210312_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
    ]
