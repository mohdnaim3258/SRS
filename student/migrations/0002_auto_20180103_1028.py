# Generated by Django 2.0.1 on 2018-01-03 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='createby',
            new_name='createdby',
        ),
    ]
