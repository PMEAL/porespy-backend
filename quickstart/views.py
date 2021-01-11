from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
# from .permissions import IsAdminOrIsSelf
from rest_framework.decorators import action
# from rest_framework import ListAPIView
from quickstart.serializers import UserSerializer, GroupSerializer, GeneratorBlobsSerializer
from .models import GeneratorBlobs


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


class GeneratorsBlobsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows user to interact with the "Blobs" function inside the "Generators" module.
    """
    queryset = GeneratorBlobs.objects.all().order_by('porosity')
    serializer_class = GeneratorBlobsSerializer



