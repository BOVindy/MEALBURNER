# Generated by Django 2.2.2 on 2019-06-26 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mealburner_app', '0002_auto_20190626_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]