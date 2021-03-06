# Generated by Django 4.0.5 on 2022-06-19 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import watch.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch', '0002_remove_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('picture', models.ImageField(null=True, upload_to=watch.models.user_directory_path, verbose_name='Picture')),
                ('caption', models.TextField(max_length=300, verbose_name='Caption')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
