# Generated by Django 2.2.6 on 2019-11-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20191104_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='participant',
            new_name='numOfParticipants',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='creator',
            new_name='user',
        ),
    ]