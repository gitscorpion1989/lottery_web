# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_auto_20150424_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='lo_result',
            name='winner',
            field=models.CharField(default=b'None', max_length=200),
        ),
    ]
