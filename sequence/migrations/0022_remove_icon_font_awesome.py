# Generated by Django 3.0.3 on 2020-09-01 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0021_auto_20200901_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icon',
            name='font_awesome',
        ),
    ]
