# Generated by Django 2.1.5 on 2019-06-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userExtends', '0006_auto_20190528_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='', max_length=7),
        ),
    ]
