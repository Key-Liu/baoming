# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_other_interview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_shortcut',
            field=models.CharField(help_text=b'\xe9\x83\xa8\xe9\x97\xa8\xe7\xae\x80\xe5\x86\x99', max_length=5),
        ),
    ]
