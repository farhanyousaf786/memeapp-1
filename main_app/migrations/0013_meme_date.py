# Generated by Django 4.1 on 2022-09-08 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_rename_commentcontent_comment_text_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='date',
            field=models.CharField(default=datetime.datetime(2022, 9, 8, 16, 38, 26, 792252, tzinfo=datetime.timezone.utc), max_length=10),
        ),
    ]