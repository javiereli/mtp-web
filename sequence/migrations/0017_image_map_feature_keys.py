# Generated by Django 3.0.3 on 2020-10-25 19:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0016_auto_20201020_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='map_feature_keys',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None), blank=True, null=True, size=None),
        ),
    ]