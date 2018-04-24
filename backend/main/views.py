# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import PersonSerializer
from .models import Person
from .tasks import generate_user_list


class PersonViewSet(
    GenericViewSet,
    CreateModelMixin,
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GeneratePersonList(APIView):
    def get(self, request):
        generate_user_list.delay()

        return Response(status=HTTP_200_OK)


class RetrievePersonListFile(APIView):
    def get(self, request):
        with open(settings.FILE_LOCATION, 'r') as data:
            content = data.read()

        return Response(status=HTTP_200_OK, data=json.loads(content))
