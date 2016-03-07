# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_date', models.DateTimeField(null=True, editable=False, blank=True)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
                ('is_expired', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('priority', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=60)),
                ('title_slug', models.SlugField(max_length=60, editable=False)),
                ('content', models.TextField()),
                ('created_by', models.ForeignKey(related_name='luzfcb_todo_task_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='luzfcb_todo_task_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_date', models.DateTimeField(null=True, editable=False, blank=True)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
                ('is_expired', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('priority', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=60)),
                ('name_slug', models.SlugField(max_length=60, editable=False)),
                ('created_by', models.ForeignKey(related_name='luzfcb_todo_todolist_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='luzfcb_todo_todolist_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='task',
            name='todolist',
            field=models.ForeignKey(to='luzfcb_todo.TodoList'),
        ),
    ]
