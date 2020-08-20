# Generated by Django 3.0.3 on 2020-08-16 18:38

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0003_auto_20200816_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='camera_make',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='captured_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='geometry_coordinates',
            field=django.contrib.gis.db.models.fields.LineStringField(null=True, srid=4326),
        ),
    ]
