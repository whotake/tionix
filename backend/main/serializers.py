# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'date_of_birth'
        )
