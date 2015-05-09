# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150408_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userr',
            new_name='user',
        ),
    ]
