# Generated by Django 3.0.3 on 2020-09-28 19:00

import accounts.models
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import storages.backends.s3boto3


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed for Username.')])),
                ('is_active', models.BooleanField(default=False)),
                ('is_maillist', models.BooleanField(default=False)),
                ('mapillary_access_token', models.TextField(blank=True, default='', null=True)),
                ('verify_email_key', models.CharField(default='', max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(bucket=''), upload_to=accounts.models.image_directory_path)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alpha characters are allowed for Username.')])),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alpha characters are allowed for Username.')])),
                ('website_url', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MapillaryUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('key', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('avatar', models.CharField(max_length=255, null=True)),
                ('about', models.TextField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('iamges_total_count', models.IntegerField(default=0)),
                ('sequences_total_count', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
