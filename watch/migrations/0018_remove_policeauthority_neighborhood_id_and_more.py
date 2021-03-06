# Generated by Django 4.0.5 on 2022-06-21 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch', '0017_remove_healthcentre_user_remove_policeauthority_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policeauthority',
            name='neighborhood_id',
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='HealthCentre',
        ),
        migrations.DeleteModel(
            name='PoliceAuthority',
        ),
    ]
