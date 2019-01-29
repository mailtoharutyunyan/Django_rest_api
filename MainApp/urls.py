from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from case1.views import ViewUserSet

routers = routers.DefaultRouter()
routers.register(r'task', ViewUserSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(routers.urls))
]
