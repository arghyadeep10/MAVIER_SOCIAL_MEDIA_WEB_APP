# Generated by Django 3.1.4 on 2020-12-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mavier', '0014_post_temp_like_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedpost',
            name='temp_like_flag',
            field=models.IntegerField(default=0),
        ),
    ]
