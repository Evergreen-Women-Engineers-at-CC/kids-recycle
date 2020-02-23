from django.db import models


class Trash(models.Model):
    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200, default='kids-recycle/kidsRecycle/sortingCans/media/error.png')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Recycle(models.Model):
    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200, default='kids-recycle/kidsRecycle/sortingCans/media/error.png')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Compost(models.Model):
    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200, default='kids-recycle/kidsRecycle/sortingCans/media/error.png')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
