# Generated by Django 3.0.3 on 2020-09-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0040_cameramake'),
        ('challenge', '0003_challenge_expected_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='camera_make',
            field=models.ManyToManyField(to='sequence.CameraMake'),
        ),
    ]
