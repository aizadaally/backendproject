from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from api.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]