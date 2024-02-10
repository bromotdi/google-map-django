# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import politicalplaces.fields


class Migration(migrations.Migration):

    dependencies = [
        ('politicalplaces', '0006_mapitem_parent'),
        ('example', '0002_mylocationmultiplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyLocationInlinePlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MyLocationInlineTest',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('example.mylocation',),
        ),
        migrations.AddField(
            model_name='mylocationinlineplace',
            name='parent_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.MyLocation'),
        ),
        migrations.AddField(
            model_name='mylocationinlineplace',
            name='place',
            field=politicalplaces.fields.PlaceField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='politicalplaces.PoliticalPlace'),
        ),
    ]