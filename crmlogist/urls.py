"""
URL configuration for crmlogist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from car_logistics.views import main, all_cars, new,  dispatched, terminal, loading, shipped, unloaded, archived


urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('all-cars/', all_cars, name='all_cars'),
    path('new/', new, name='new'),
    path('dispatched/', dispatched, name='dispatched'),
    path('terminal/', terminal, name='terminal'),
    path('loading/', loading, name='loading'),
    path('shipped/', shipped, name='shipped'),
    path('unloaded/', unloaded, name='unloaded'),
    path('archived/', archived, name='archived'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
