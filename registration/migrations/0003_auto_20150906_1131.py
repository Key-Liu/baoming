# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20150906_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_interview',
            name='first_batch',
            field=models.IntegerField(help_text=b'\xe7\xac\xac\xe4\xb8\x80\xe5\xbf\x97\xe6\x84\xbf\xe9\x83\xa8\xe9\x97\xa8\xe9\x9d\xa2\xe8\xaf\x95\xe6\x89\xb9\xe6\xac\xa1', null=True),
        ),
        migrations.AlterField(
            model_name='student_interview',
            name='second_batch',
            field=models.IntegerField(help_text=b'\xe7\xac\xac\xe4\xba\x8c\xe5\xbf\x97\xe6\x84\xbf\xe9\x83\xa8\xe9\x97\xa8\xe9\x9d\xa2\xe8\xaf\x95\xe6\x89\xb9\xe6\xac\xa1', null=True),
        ),
    ]
