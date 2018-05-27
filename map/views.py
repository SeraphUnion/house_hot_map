from django.shortcuts import render
from django.http import HttpResponse
from .models import taizhou

def index(request):
    maplist=taizhou.objects.all()
    return render(request, 'map/hot.html', context={
                      'maplist':maplist
                  })
# Create your views here.
