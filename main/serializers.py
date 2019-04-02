from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Picture


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'id')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('name', 'description', 'year', 'month', 'mountains',
                  'photo1',
                  'photo2',
                  'photo3',
                  'photo4',
                  'photo5',
                  'photo6')
