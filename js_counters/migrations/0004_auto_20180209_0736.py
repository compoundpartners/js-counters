# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_counters', '0003_auto_20180209_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterscontainermodel',
            name='summary',
            field=models.TextField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='counterscontainermodel',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
