# Generated by Django 3.0.3 on 2020-03-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='logo',
            field=models.ImageField(upload_to='league/static/images'),
        ),
    ]
