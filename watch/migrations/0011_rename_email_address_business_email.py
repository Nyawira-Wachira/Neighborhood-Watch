# Generated by Django 4.0.4 on 2022-06-20 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0010_rename_business_email_address_business_email_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='email_address',
            new_name='email',
        ),
    ]
