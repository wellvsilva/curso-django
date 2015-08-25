# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_perfil_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='teste',
        ),
    ]
