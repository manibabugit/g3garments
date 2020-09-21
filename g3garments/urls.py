"""g3garments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static

  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('image_upload/', views.upload_image, name='image_upload'),
    path('success', views.success, name='success'),
    path('display_images', views.display_uploaded_images, name='display_images'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('upload_jeans/', views.upload_jeans_image, name='upload_jeans'),
    path('upload_shirts/', views.upload_shirts_image, name='upload_shirts'),
    path('upload_hoodies/', views.upload_hoodies_image, name='upload_hoodies'),
    path('upload_tracks/', views.upload_tracks_image, name='upload_tracks'),
    path('list_jeans/', views.list_jeans, name='list_jeans'),
    path('list_shirts/', views.list_shirts, name='list_shirts'),
    path('list_hoodies/', views.list_hoodies, name='list_hoodies'),
    path('list_tracks/', views.list_tracks, name='list_tracks'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)