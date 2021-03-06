# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150828_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='questions_uploaded'),
        ),
    ]
