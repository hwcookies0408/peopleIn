from django.shortcuts import render


def map_index(request):
    return render(request, 'map/map_index.html')
