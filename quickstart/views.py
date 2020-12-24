from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
# from .permissions import IsAdminOrIsSelf
from rest_framework.decorators import action
# from rest_framework import ListAPIView
from rest_framework.response import Response
# from porespyBackend.quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.serializers import UserSerializer, GroupSerializer, HeroSerializer, PoreSpyGeneratorSerializer  # , TestSerializer
from .models import Hero, PoreSpyGenerator
import os
import porespy as ps
import matplotlib.pyplot as plt


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class PoreSpyViewSet(viewsets.ModelViewSet):
    queryset = PoreSpyGenerator.objects.all().order_by('porosity')
    serializer_class = PoreSpyGeneratorSerializer


