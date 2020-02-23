from django.db import models


class Trash(models.Model):
    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200, default='kids-recycle/kidsRecycle/sortingCans/media/error.png')
    points = models.IntegerField(default=0)


<<<<<<< HEAD

=======
>>>>>>> 39d9c02bb8bc9a995a1590591dc255da3ad7398b
class Recycle(models.Model):
    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200, default='kids-recycle/kidsRecycle/sortingCans/media/error.png')
    points = models.IntegerField(default=0)


class Compost(models.Model):
    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200, default='kids-recycle/kidsRecycle/sortingCans/media/error.png')
    points = models.IntegerField(default=0)

# Create your models here.
