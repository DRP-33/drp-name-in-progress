# Generated by Django 3.2.3 on 2021-06-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210603_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10),
        ),
    ]
