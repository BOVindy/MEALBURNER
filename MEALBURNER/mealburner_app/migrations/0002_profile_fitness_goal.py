# Generated by Django 2.2.2 on 2019-07-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealburner_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fitness_goal',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]