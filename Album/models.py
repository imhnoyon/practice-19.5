from django.db import models
from Musician.models import MusicianModel
from datetime import date
# Create your models here.

class AlbumModel(models.Model):
    Album_name = models.CharField(max_length=255)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    release_date = models.DateField(default=date.today)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name