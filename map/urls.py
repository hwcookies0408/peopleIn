from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('', views.map_index, name='map_index'),
]
