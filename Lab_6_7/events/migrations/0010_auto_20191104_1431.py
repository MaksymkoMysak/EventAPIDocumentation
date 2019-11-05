# Generated by Django 2.2.6 on 2019-11-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20191104_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='participant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='numOfCreatedEvents',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='numOfParticipatingEvents',
            field=models.IntegerField(default=0),
        ),
    ]
