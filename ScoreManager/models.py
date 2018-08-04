from django.db import models
from django.contrib import admin

class Student(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    chinese = models.FloatField()
    math = models.FloatField()
    english = models.FloatField()
    physics = models.FloatField()
    chemistry = models.FloatField()
    summary = models.FloatField()