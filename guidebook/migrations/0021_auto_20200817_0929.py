# Generated by Django 3.0.3 on 2020-08-17 08:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0020_auto_20200813_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='tag',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='0', max_length=6), null=True, size=None),
        ),
    ]
