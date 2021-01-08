# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='sms.Student'),
        ),
    ]
