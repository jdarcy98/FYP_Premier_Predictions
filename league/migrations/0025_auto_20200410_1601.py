# Generated by Django 3.0.3 on 2020-04-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0024_finalscores'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpredictions',
            name='points',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='away_score',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='home_score',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, null=True),
        ),
    ]
