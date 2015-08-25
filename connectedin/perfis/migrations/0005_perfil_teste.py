# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20150731_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='teste',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
