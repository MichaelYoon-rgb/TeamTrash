from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import Locations
from django.core import serializers

# assuming obj is a model instance

def index(request):
    mapbox_access_token = 'pk.eyJ1IjoibWljaGFlbDQ0NDQiLCJhIjoiY2w3YnpjemMzMDg5ZDNwb2w2eW0wM2JpMSJ9.KWknsMC43nNrTuMnwOfRwg'
    context = {'Locations': Locations.objects.all, 'NumLocations': Locations.objects.count(), 'mapbox_access_token': mapbox_access_token}
    return HttpResponse(render(request, 'detectTrash/index.html', context ))

def getLocations(request):
    data = serializers.serialize('json', Locations.objects.all())
    return HttpResponse(data, content_type='application/json')

def setLocations(request):
    
    try:
        if request.method == 'POST':
            
            latitude = request.POST.get('post[latitude]')
            longitude = request.POST.get('post[longitude]')
            goal = request.POST.get('post[goal]')
            print(goal)
            Locations.objects.create(latitude = float(latitude), longitude = float(longitude), goal=int(goal))
    except Exception:
        return HttpResponseBadRequest()
    return HttpResponse()