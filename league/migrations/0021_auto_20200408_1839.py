# Generated by Django 3.0.3 on 2020-04-08 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0020_auto_20200408_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpredictions',
            name='match',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.FixtureInfo'),
        ),
    ]