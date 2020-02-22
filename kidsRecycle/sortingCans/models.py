from django.db import models

class Trash(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

class Recycle(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

class Compost(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)


# Create your models here.
