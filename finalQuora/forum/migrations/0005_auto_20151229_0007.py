# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20150902_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(related_name='answers', to='forum.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='views',
            field=models.ForeignKey(null=True, related_name='a_MyUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
