# Generated by Django 4.1.1 on 2022-09-05 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Photo',
        ),
    ]
