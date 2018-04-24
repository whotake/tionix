# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.conf import settings
from celery import shared_task

from .models import Person
from .serializers import json_serial


@shared_task
def generate_user_list():
    persons = Person.objects.all().values(
        'first_name', 'last_name', 'middle_name', 'date_of_birth'
    )

    with open(settings.FILE_LOCATION, 'w') as to_export:
        json.dump(list(persons), to_export, sort_keys=True, indent=4,
                  ensure_ascii=False, default=json_serial)

        to_export.close()
