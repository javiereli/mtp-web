# Generated by Django 3.0.3 on 2020-08-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200722_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mapillary_access_token',
            field=models.TextField(default='', null=True),
        ),
    ]
