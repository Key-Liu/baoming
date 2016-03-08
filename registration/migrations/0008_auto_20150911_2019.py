# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20150911_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_number',
            field=models.IntegerField(default=0, help_text=b'\xe9\x83\xa8\xe9\x97\xa8\xe9\x9d\xa2\xe8\xaf\x95\xe4\xba\xba\xe6\x95\xb0', null=True, blank=True),
        ),
    ]
