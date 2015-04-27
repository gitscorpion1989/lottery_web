# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0003_lo_result_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lo_result',
            name='winner',
            field=models.CharField(default=b'NO WINNER', max_length=200),
        ),
    ]
