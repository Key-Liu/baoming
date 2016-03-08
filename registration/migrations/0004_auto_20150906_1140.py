# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20150906_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_interview',
            name='first_dept',
            field=models.ForeignKey(related_name='first_dept', to='registration.Department', null=True),
        ),
        migrations.AlterField(
            model_name='student_interview',
            name='second_dept',
            field=models.ForeignKey(related_name='second_dept', to='registration.Department', null=True),
        ),
    ]
