# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from .views import RetrievePersonListFile, GeneratePersonList, PersonViewSet

router = SimpleRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    url(r'^retrieve/$', RetrievePersonListFile.as_view(), name='retrieve'),
    url(r'^generate/$', GeneratePersonList.as_view(), name='generate'),
]

urlpatterns += router.urls
