# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import get_object_or_404
from pip._vendor.html5lib import serializer
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from . searializers import employeeSerializers
from . models import employees


# Create your views here.
class employeeList(APIView):

    def get(self,request):

        employee1= employees.objects.all()
        serializer=employeeSerializers(employee1, many=True)
        return Response(serializer.data)


    def post(self):
        pass