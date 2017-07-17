# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 07:15
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ITAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('model_type', models.CharField(blank=True, max_length=32, null=True)),
                ('name', models.CharField(db_index=True, max_length=512, null=True)),
                ('ip_set', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='IP地址')),
                ('mac_address_set', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='MAC地址')),
                ('management_port', models.IntegerField(default=22, verbose_name='管理端口')),
                ('idc_location', models.CharField(blank=True, max_length=512, null=True, verbose_name='IDC机房位置')),
                ('hardware_type', models.CharField(blank=True, max_length=512, null=True)),
                ('cpu', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='CPU配置')),
                ('memory', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('disk', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('network_card', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('os_type', models.CharField(blank=True, max_length=32, null=True)),
                ('os_version', models.CharField(blank=True, max_length=32, null=True)),
                ('asset_number', models.CharField(blank=True, max_length=128, null=True)),
                ('sn', models.CharField(blank=True, max_length=128, null=True)),
                ('cabinet_number', models.CharField(blank=True, max_length=128, null=True)),
                ('server_location', models.CharField(blank=True, max_length=512, null=True)),
                ('server_type', models.CharField(blank=True, max_length=128, null=True)),
                ('run_env', models.CharField(blank=True, max_length=128, null=True)),
                ('server_status', models.CharField(blank=True, max_length=128, null=True)),
                ('put_shelf_time', models.DateTimeField(verbose_name='上架时间')),
                ('has_activated', models.BooleanField(default=False, verbose_name='是否激活')),
                ('description', models.TextField(blank=True, null=True, verbose_name='备注信息')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]