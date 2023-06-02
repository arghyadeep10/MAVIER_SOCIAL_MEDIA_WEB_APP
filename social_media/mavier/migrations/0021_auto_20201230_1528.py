# Generated by Django 3.1.4 on 2020-12-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mavier', '0020_auto_20201230_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notification_type',
            field=models.CharField(blank=True, choices=[('Post_Like', 'Post Like'), ('SharedPost_Like', 'SharedPost Like'), ('Post_Comment', 'Post Comment'), ('SharedPost_Comment', 'SharedPost Comment'), ('Post_Shared', 'Post_Shared'), ('New_Follower', 'New_Follower')], max_length=100, null=True),
        ),
    ]
