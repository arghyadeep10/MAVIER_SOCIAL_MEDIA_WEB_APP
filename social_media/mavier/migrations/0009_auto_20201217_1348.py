# Generated by Django 3.1.4 on 2020-12-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mavier', '0008_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]