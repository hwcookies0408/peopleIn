# Generated by Django 2.1.5 on 2019-06-03 01:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0002_remove_notice_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]