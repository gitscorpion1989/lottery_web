# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lo_Result_Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cur_phase', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameField(
            model_name='lo_result',
            old_name='Phase',
            new_name='phase',
        ),
    ]
