from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .Serializers import User, UserSerializers


class ViewUserSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-dob')
    serializer_class = UserSerializers
