# Generated by Django 3.0.3 on 2020-04-09 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0023_auto_20200409_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_fs', models.DecimalField(decimal_places=0, max_digits=2, null=True)),
                ('away_fs', models.DecimalField(decimal_places=0, max_digits=2, null=True)),
                ('result', models.CharField(choices=[('H', 'Home win'), ('A', 'Away win'), ('D', 'Draw')], max_length=1)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.FixtureInfo')),
            ],
        ),
    ]
