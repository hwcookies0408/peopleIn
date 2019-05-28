# Generated by Django 2.1.5 on 2019-05-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userExtends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AddField(
            model_name='profile',
            name='in_area',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Gangnam'), (2, 'Sungdong'), (3, 'Yeongdeungpo'), (4, 'Gwangjin'), (5, 'Mapo'), (6, 'Songpa')], null=True),
        ),
    ]