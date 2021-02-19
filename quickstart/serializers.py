from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Blobs, BundleOfTubes, PoreSpyFuncsNames


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GeneratorBlobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blobs
        fields = ['porosity', 'blobiness', 'dimension_x', 'dimension_y', 'dimension_z', 'generated_image']


class GeneratorBundleOfTubesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BundleOfTubes
        fields = ['dimension_x', 'dimension_y', 'dimension_z', 'spacing', 'generated_image']


class PoreSpyFuncsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoreSpyFuncsNames
        fields = ['porespy_funcs']

