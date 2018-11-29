# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounterModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='js_counters_countermodel', primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CountersContainerModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='js_counters_counterscontainermodel', primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True, serialize=False)),
                ('bg_image', models.ImageField(blank=True, upload_to='media/images', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
