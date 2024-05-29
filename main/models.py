from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255,unique=True)

class CalculationResult(models.Model):
    A = models.IntegerField()
    B = models.IntegerField()
    K1 = models.FloatField()
    mark = models.IntegerField()
    A1 = models.IntegerField()
    B1 = models.IntegerField()
    K2 = models.FloatField()
    mark1 = models.IntegerField()