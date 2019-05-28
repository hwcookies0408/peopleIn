from django.urls import path


from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('<int:pk>/', views.notice_detail, name='notice_detail'),
    path('new/', views.new_feed, name='new_feed'),
]