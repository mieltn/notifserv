# Generated by Django 4.1.1 on 2022-09-19 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_client_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailinglist',
            old_name='endDatetime',
            new_name='expDatetime',
        ),
        migrations.RenameField(
            model_name='mailinglist',
            old_name='sendDatetime',
            new_name='startDatetime',
        ),
    ]
