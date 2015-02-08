from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from wanderer.models import Location

def index(request):
  return render(request, 'wanderer/test.html')

def link(request, location_id):
  loc = get_object_or_404(Location, pk=location_id)
  return redirect('https://www.google.com/maps/place/{},{}'.format(loc.latitude, 
loc.longitude))
  return HttpResponse('id {}'.format(location_id))
