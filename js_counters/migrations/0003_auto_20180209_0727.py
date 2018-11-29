# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_counters', '0002_auto_20180206_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterscontainermodel',
            name='button_link',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='counterscontainermodel',
            name='button_text',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
    ]
