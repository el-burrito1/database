# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player_lite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
