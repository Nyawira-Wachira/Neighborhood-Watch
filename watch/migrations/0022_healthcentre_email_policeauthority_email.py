# Generated by Django 4.0.5 on 2022-06-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0021_post_neighborhood_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcentre',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='policeauthority',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
