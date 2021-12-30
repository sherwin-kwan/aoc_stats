from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import PuzzleSerializer
from .models import Puzzle

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class PuzzleViewSet(viewsets.ModelViewSet):
  queryset = Puzzle.objects.all().order_by('name')
  serializer_class = PuzzleSerializer