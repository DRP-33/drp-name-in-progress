# Generated by Django 3.2.3 on 2021-06-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=256)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
