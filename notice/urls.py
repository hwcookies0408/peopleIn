from django.urls import path
from notice import views

app_name = 'notice'

urlpatterns = [
    # 공지사항
    path('', views.notice_list, name='notice_list'),
    path('<int:pk>/', views.notice_detail, name='notice_detail'),
    path('new/', views.notice_new, name='notice_new'),  # 등록
    path('remove/<int:pk>/', views.notice_remove, name='notice_remove'),  # 삭제
    path('edit/<int:pk>/', views.notice_edit, name='notice_edit'),  # 수정

    # 프랜차이즈
    path('franchise/', views.franchise_list, name='franchise_list'),
    path('franchise/<int:pk>/', views.franchise_detail, name='franchise_detail'),
    path('franchise/new/', views.franchise_new, name='franchise_new'),  # 등록
    path('franchise/remove/<int:pk>/', views.franchise_remove, name='franchise_remove'),  # 삭제
    path('franchise/edit/<int:pk>/', views.franchise_edit, name='franchise_edit'),  # 수정
]