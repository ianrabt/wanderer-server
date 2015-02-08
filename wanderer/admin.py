from django.contrib import admin
from wanderer.models import Location, Perspective, Rating

class PerspectiveInline(admin.TabularInline):
  model = Perspective
  extra = 0

class RatingInline(admin.TabularInline):
  model = Rating
  extra = 0

class LocationAdmin(admin.ModelAdmin):
  inlines = [PerspectiveInline, RatingInline]

admin.site.register(Location, LocationAdmin)
