from django.db import models


class Location(models.Model):
  address = models.CharField(max_length=200, default='unknown', blank=True)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  
  def __str__(self):
    return '{}@({}, {})'.format(self.address, self.latitude, self.longitude)

class Perspective(models.Model):
  location = models.ForeignKey(Location)
  photo = models.ImageField(upload_to='photos')
  description = models.TextField(blank=True, null=True)
  date = models.DateTimeField()
  author = models.CharField(max_length=200, blank=True, null=True)
