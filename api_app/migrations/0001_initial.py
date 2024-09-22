# Generated by Django 5.0.3 on 2024-09-20 21:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=125)),
                ('lastName', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=125, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=125)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
