# Generated by Django 2.2.5 on 2021-02-21 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20210129_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='contry',
            new_name='country',
        ),
    ]
