# Generated by Django 3.0.3 on 2020-04-04 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0010_auto_20200404_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpredictions',
            name='match_id',
        ),
        migrations.RemoveField(
            model_name='userpredictions',
            name='user',
        ),
        migrations.DeleteModel(
            name='FixtureInfo',
        ),
        migrations.DeleteModel(
            name='UserPredictions',
        ),
    ]