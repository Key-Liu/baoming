# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20150906_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other_interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_batch', models.IntegerField(help_text=b'\xe7\xac\xac\xe4\xb8\x80\xe5\xbf\x97\xe6\x84\xbf\xe9\x83\xa8\xe9\x97\xa8\xe9\x9d\xa2\xe8\xaf\x95\xe6\x89\xb9\xe6\xac\xa1', null=True)),
                ('second_batch', models.IntegerField(help_text=b'\xe7\xac\xac\xe4\xba\x8c\xe5\xbf\x97\xe6\x84\xbf\xe9\x83\xa8\xe9\x97\xa8\xe9\x9d\xa2\xe8\xaf\x95\xe6\x89\xb9\xe6\xac\xa1', null=True)),
                ('first_dept', models.ForeignKey(related_name='other_first_dept', to='registration.Department', null=True)),
                ('second_dept', models.ForeignKey(related_name='other_second_dept', to='registration.Department', null=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
    ]
