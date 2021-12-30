from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Puzzle

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ["url", "username", "email", "groups"]

class PuzzleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Puzzle
    fields = ["name", "year", "day"]