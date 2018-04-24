from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    # API endpoint
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # API endpoint
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
