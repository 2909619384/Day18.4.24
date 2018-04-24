# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=6, unique=True)),
                ('stu_dex', models.BooleanField(default=0)),
                ('stu_birth', models.DateField()),
                ('stu_create_time', models.DateField(auto_now_add=True)),
                ('stu_opera_time', models.DateField(auto_now=True)),
                ('stu_tel', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'stu',
            },
        ),
    ]
