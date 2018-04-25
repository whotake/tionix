# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from .settings import API_URL


def create_person(data):
    return requests.post('{0}{1}'.format(API_URL, '/persons/'), data=data)


def retrieve_persons():
    return requests.get('{0}{1}'.format(API_URL, '/retrieve/'))


def generate_records():
    return requests.get('{0}{1}'.format(API_URL, '/generate/'))
