# Generated by Django 3.0.3 on 2020-04-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0012_fixtureinfo_userpredictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpredictions',
            name='away_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='home_score',
            field=models.IntegerField(),
        ),
    ]
