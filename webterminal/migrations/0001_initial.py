# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name=b'Credential name')),
                ('method', models.CharField(choices=[(b'password', b'password'), (b'key', b'key')], max_length=40)),
                ('key', models.TextField(blank=True)),
                ('password', models.CharField(blank=True, max_length=40)),
                ('proxy', models.BooleanField(default=False)),
                ('proxyserverip', models.GenericIPAddressField(protocol=b'ipv4')),
                ('proxyport', models.PositiveIntegerField(blank=True, default=22)),
                ('proxyrequired', models.BooleanField(default=False)),
                ('proxypassword', models.CharField(max_length=40, verbose_name=b'Proxy password')),
            ],
        ),
        migrations.CreateModel(
            name='ServerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedatetime', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('createdatetime', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Server group name')),
            ],
        ),
        migrations.CreateModel(
            name='ServerInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedatetime', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('onlinedatetime', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Server name')),
                ('hostname', models.CharField(blank=True, max_length=40, verbose_name=b'Host name')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4')),
                ('credential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webterminal.Credential')),
            ],
        ),
        migrations.AddField(
            model_name='servergroup',
            name='servers',
            field=models.ManyToManyField(related_name='servers', to='webterminal.ServerInformation'),
        ),
    ]