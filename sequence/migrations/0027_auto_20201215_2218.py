# Generated by Django 3.0.3 on 2020-12-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_setting', '0007_auto_20201208_1121'),
        ('sequence', '0026_remove_sequence_static_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='sys_setting.Tag'),
        ),
    ]