# Generated by Django 3.0.3 on 2020-03-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to='prof_pics'),
        ),
    ]
