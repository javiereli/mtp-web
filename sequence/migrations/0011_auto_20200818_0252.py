# Generated by Django 3.0.3 on 2020-08-18 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0010_sequence_transport_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='transport_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sequence.TransportType'),
        ),
    ]
