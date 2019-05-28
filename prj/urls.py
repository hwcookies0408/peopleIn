from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings                         # 추가 1
from django.conf.urls.static import static

from .views import UserCreateView, UserCreateDoneTV
from . import views


urlpatterns = [
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    # 계정 가입 처리하는 URL
    re_path(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    # 계정 가입 완료될 때 보여줄 URL
    re_path(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('map/', include('map.urls')),
    path('notice/', include('notice.urls')),
    path('analysis/', include('analysis.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:                                       # 추가 2
    import debug_toolbar                                 # 추가 2
    urlpatterns += [                                     # 추가 2
        path('__debug__/', include(debug_toolbar.urls)), # 추가 2
    ]                                                    # 추가 2
