# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0002_auto_20171018_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='opinion',
            name='agrees',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='disagrees',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
