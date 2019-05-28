# Generated by Django 2.1.5 on 2019-05-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userExtends', '0002_auto_20190526_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='in_area',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '강남구'), (2, '성동구'), (3, '영등포구'), (4, '광진구'), (5, '마포구'), (6, '송파구')], null=True),
        ),
    ]