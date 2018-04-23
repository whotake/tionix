# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    middle_name = models.CharField(max_length=40, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name
