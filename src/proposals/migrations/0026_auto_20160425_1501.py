# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-25 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0025_auto_20160418_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalspeaker',
            options={'ordering': ['proposal_type', 'proposal_id', 'pk'], 'verbose_name': 'additional speaker', 'verbose_name_plural': 'additional speakers'},
        ),
    ]
