# Generated by Django 4.0.5 on 2022-06-19 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
