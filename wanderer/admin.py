from django.contrib import admin
from wanderer.models import Location, Perspective

class PerspectiveInline(admin.TabularInline):
  model = Perspective
  extra = 1

class LocationAdmin(admin.ModelAdmin):
  inlines = [PerspectiveInline]

admin.site.register(Location, LocationAdmin)
