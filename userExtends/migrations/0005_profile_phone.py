# Generated by Django 2.1.5 on 2019-05-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userExtends', '0004_remove_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
