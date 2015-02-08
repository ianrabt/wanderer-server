from django.db import models

class Location(models.Model):
  address = models.CharField(max_length=200, default='unknown', blank=True)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  
  # rating_avg = models.DecimalField(max_digits=11, decimal_places=10, blank=True, null=True)
  # rating_count = models.IntegerField(default=0)
  
  def __str__(self):
    return '{}@({}, {})'.format(self.address, self.latitude, self.longitude)

class Perspective(models.Model):
  photo = models.ImageField(upload_to='photos')
  description = models.TextField(blank=True, null=True)
  date = models.DateTimeField()

  location = models.ForeignKey(Location)
  author = models.CharField(max_length=200)

class Rating(models.Model):
  CHOICES = enumerate({1, 2, 3, 4, 5})
  rating = models.IntegerField(choices=CHOICES)

  location = models.ForeignKey(Location)
  author = models.CharField(max_length=200)
