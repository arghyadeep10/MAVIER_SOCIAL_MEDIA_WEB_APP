# Generated by Django 3.1.4 on 2020-12-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mavier', '0013_auto_20201228_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='temp_like_flag',
            field=models.IntegerField(default=0),
        ),
    ]
