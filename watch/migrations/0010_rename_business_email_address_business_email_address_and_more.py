# Generated by Django 4.0.4 on 2022-06-20 18:24

from django.db import migrations, models
import django.utils.timezone
import watch.models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0009_business'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_email_address',
            new_name='email_address',
        ),
        migrations.AddField(
            model_name='business',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=watch.models.user_directory_path, verbose_name='Picture'),
            preserve_default=False,
        ),
    ]
