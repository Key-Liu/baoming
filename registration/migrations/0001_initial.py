# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_name', models.CharField(help_text=b'\xe9\x83\xa8\xe9\x97\xa8\xe5\x90\x8d\xe7\xa7\xb0', max_length=4)),
                ('department_info', models.CharField(help_text=b'\xe9\x83\xa8\xe9\x97\xa8\xe7\xae\x80\xe4\xbb\x8b', max_length=140, null=True, blank=True)),
                ('department_shortcut', models.CharField(help_text=b'\xe9\x83\xa8\xe9\x97\xa8\xe7\xae\x80\xe5\x86\x99', max_length=4)),
                ('department_number', models.IntegerField(help_text=b'\xe9\x83\xa8\xe9\x97\xa8\xe9\x9d\xa2\xe8\xaf\x95\xe4\xba\xba\xe6\x95\xb0', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interview_batch', models.IntegerField(help_text=b'\xe9\x9d\xa2\xe8\xaf\x95\xe6\x89\xb9\xe6\xac\xa1')),
                ('interview_dept', models.ForeignKey(to='registration.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.CharField(help_text=b'\xe5\xad\xa6\xe5\x8f\xb7', max_length=12)),
                ('student_name', models.CharField(help_text=b'\xe5\xa7\x93\xe5\x90\x8d', max_length=50)),
                ('class_num', models.IntegerField(help_text=b'\xe7\x8f\xad\xe7\xba\xa7\xef\xbc\x8c\xe8\x8c\x83\xe5\x9b\xb4\xe4\xb8\xba1-7\xef\xbc\x8c7\xe4\xb8\xba\xe5\x8d\x93\xe8\xb6\x8a\xe7\x89\x88')),
                ('doom_num', models.CharField(help_text=b'\xe5\xae\xbf\xe8\x88\x8d\xe5\x8f\xb7\xe7\xa0\x81', max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='interview_student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='choice',
            name='first_choice',
            field=models.ForeignKey(related_name='first_choice', to='registration.Department', help_text=b'\xe7\xac\xac\xe4\xb8\x80\xe5\xbf\x97\xe6\x84\xbf', null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='second_choice',
            field=models.ForeignKey(related_name='seconde_choide', to='registration.Department', help_text=b'\xe7\xac\xac\xe4\xba\x8c\xe5\xbf\x97\xe6\x84\xbf', null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='student',
            field=models.ForeignKey(help_text=b'\xe5\xad\xa6\xe5\x8f\xb7', to='registration.Student'),
        ),
    ]
