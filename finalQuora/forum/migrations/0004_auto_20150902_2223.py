# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20150828_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.ForeignKey(null=True, related_name='questions_viewed', to=settings.AUTH_USER_MODEL),
        ),
    ]
