# Generated by Django 3.0.3 on 2020-04-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0013_auto_20200405_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpredictions',
            name='away_score',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='home_score',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
