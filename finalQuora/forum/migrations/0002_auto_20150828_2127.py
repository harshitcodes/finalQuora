# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='by',
            field=models.ForeignKey(related_name='quesitons_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.ForeignKey(related_name='questions_viewed', to=settings.AUTH_USER_MODEL),
        ),
    ]
