# Generated by Django 3.1.4 on 2020-12-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201227_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, help_text='Should be in yyyy-mm-dd format', null=True),
        ),
    ]
