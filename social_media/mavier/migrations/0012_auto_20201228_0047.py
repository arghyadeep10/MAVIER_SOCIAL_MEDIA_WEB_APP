# Generated by Django 3.1.4 on 2020-12-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mavier', '0011_comment_forsharedpost_like_for_sharedpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
