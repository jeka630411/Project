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

# class College(models.Model):
#     title = models.TextField(max_length=255)
#     rating = models.FloatField(default=0)
#
#     def __str__(self):
#         return f"College: {self.title}, rating: {self.rating}"


class Rating(models.Model):
    total_score = models.FloatField()

    def __str__(self):
        return f"Rating: {self.total_score}"