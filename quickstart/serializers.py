from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response
# from quickstart.models import Test
from .models import Hero, PoreSpyTutorial

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'alias', 'height']


class PoreSpyTutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoreSpyTutorial
        fields = ['porosity', 'blobiness', 'dimension_x', 'dimension_y', 'generated_image']

