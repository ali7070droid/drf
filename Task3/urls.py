"""Task3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Music.views import Artist_list,album_list,track_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Artist_list, name='Artist_list'),
    path('album_list/<int:pk>',album_list, name='album_list'),
    path('track_list/<int:pk>',track_list, name='track_list'),
    path('',include('Music.urls')),
]
