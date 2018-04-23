# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import PersonSerializer
from .models import Person


class PersonViewSet(
    GenericViewSet,
    CreateModelMixin,
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GeneratePersonList(APIView):
    def get(self, request):
        persons = Person.objects.all()

        with open(settings.FILE_LOCATION, 'w') as to_export:
            to_export.truncate(0)

            for person in persons:
                to_export.write('{0} {1} {2}\n'.format(
                    person.first_name,
                    person.last_name,
                    person.middle_name
                ))

            to_export.close()

        return Response(status=HTTP_200_OK)


class RetrievePersonListFile(APIView):
    def get(self, request):
        with open(settings.FILE_LOCATION, 'r') as data:
            content = data.read()

        return Response(status=HTTP_200_OK, data=content)
