# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from common.CommonRes import *
from django.conf import settings
from .service import TestService

# Create your views here.

class ApiViewSet(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        configs = getattr(settings, 'CONFIGS', None)
        res["result"] = configs

        TestService.testService(res)

        return Response(res, status=200)

