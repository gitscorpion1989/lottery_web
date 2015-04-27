# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lo_bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phase', models.IntegerField()),
                ('bet_date', models.DateTimeField(verbose_name=b'time of draw lottery result')),
                ('re1', models.IntegerField(default=-1)),
                ('re2', models.IntegerField(default=-1)),
                ('re3', models.IntegerField(default=-1)),
                ('re4', models.IntegerField(default=-1)),
                ('re5', models.IntegerField(default=-1)),
                ('re6', models.IntegerField(default=-1)),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
