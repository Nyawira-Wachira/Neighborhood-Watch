# Generated by Django 4.0.5 on 2022-06-21 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0019_policeauthority_healthcentre'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='neighborhood_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watch.neighborhood'),
        ),
    ]
