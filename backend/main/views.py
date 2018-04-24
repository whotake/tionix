# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import PersonSerializer, json_serial
from .models import Person


class PersonViewSet(
    GenericViewSet,
    CreateModelMixin,
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GeneratePersonList(APIView):
    def get(self, request):
        persons = Person.objects.all().values(
            'first_name', 'last_name', 'middle_name', 'date_of_birth'
        )

        with open(settings.FILE_LOCATION, 'w') as to_export:
            json.dump(list(persons), to_export, sort_keys=True, indent=4,
                      ensure_ascii=False, default=json_serial)

            to_export.close()

        return Response(status=HTTP_200_OK)


class RetrievePersonListFile(APIView):
    def get(self, request):
        with open(settings.FILE_LOCATION, 'r') as data:
            content = data.read()

        return Response(status=HTTP_200_OK, data=json.loads(content))
