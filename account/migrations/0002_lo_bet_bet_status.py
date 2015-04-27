# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lo_bet',
            name='bet_status',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Pending'), (b'W', b'Win!'), (b'M', b'Miss')]),
        ),
    ]
