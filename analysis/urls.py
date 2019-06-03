from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.analysis_list, name='analysis_list'),
    path('people/', views.analysis_people, name='analysis_people'),

]
