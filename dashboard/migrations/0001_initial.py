# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBalance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.FloatField(default=0)),
                ('change_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('current_location', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('abstractbalance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.AbstractBalance')),
            ],
            bases=('dashboard.abstractbalance',),
        ),
        migrations.CreateModel(
            name='BalanceHistory',
            fields=[
                ('abstractbalance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.AbstractBalance')),
            ],
            options={
                'ordering': ['-pk'],
            },
            bases=('dashboard.abstractbalance',),
        ),
    ]
