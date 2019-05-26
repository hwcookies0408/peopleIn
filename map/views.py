from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def map_index(request):
    return render(request, 'map/map_index.html')
