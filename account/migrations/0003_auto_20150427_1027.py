# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_lo_bet_bet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lo_bet',
            name='bet_status',
            field=models.CharField(default=b'Pending', max_length=7),
        ),
    ]
