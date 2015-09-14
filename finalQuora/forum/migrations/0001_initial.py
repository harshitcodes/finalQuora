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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.TextField(max_length=10000)),
                ('desc', models.TextField(verbose_name='Description', max_length=50, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('heading', models.TextField(max_length=500)),
                ('desc', models.TextField(max_length=1000, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('related_pic', models.ImageField(upload_to='Topic_Pics/', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ManyToManyField(related_name='related_topic', to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='question',
            name='views',
            field=models.ForeignKey(related_name='q_MyUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(to='forum.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='views',
            field=models.ForeignKey(related_name='a_MyUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
