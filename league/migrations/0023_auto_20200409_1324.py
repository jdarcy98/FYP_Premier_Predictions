# Generated by Django 3.0.3 on 2020-04-09 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0022_auto_20200409_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpredictions',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.FixtureInfo'),
        ),
    ]
