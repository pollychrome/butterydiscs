from django.db import models

class Disc(models.Model):
    image = models.ImageField(upload_to='disc_images')
    description = models.TextField()
    speed = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)