# Generated by Django 3.0.6 on 2020-06-01 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20200601_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocieresshoppinglist',
            old_name='uesr',
            new_name='user',
        ),
    ]