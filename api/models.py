from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Puzzle(models.Model):
  name = models.CharField(max_length = 255, null=True)
  year = models.IntegerField()
  day = models.IntegerField()
  first_silver = models.IntegerField(null=True)
  first_gold = models.IntegerField(null=True)
  hundredth_silver = models.IntegerField(null=True)
  hundredth_gold = models.IntegerField(null=True) 

  def __str__(name):
    return "Not implemented"

class Record(models.Model):
  puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
  seconds = models.IntegerField()
  position = models.IntegerField()
  part = models.IntegerField(null=True)