# Generated by Django 3.1.6 on 2021-03-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0019_auto_20210302_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
    ]
