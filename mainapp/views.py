from django.shortcuts import render, redirect, HttpResponse
from rest_framework import viewsets

from .serializers import SerializeStudent
from .models import StudentDetails


# REST API CLASS
class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all().order_by('name')
    serializer_class = SerializeStudent
