# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_counters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countermodel',
            old_name='name',
            new_name='counter_text',
        ),
        migrations.RenameField(
            model_name='countermodel',
            old_name='value',
            new_name='counter_value',
        ),
    ]
