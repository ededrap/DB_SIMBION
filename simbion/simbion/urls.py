"""simbion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('beasiswa/daftar/', include('daftar_beasiswa.urls', namespace='daftar-beasiswa')),
    path('beasiswa/lihat/', include('lihat_beasiswa.urls', namespace='lihat-beasiswa')),
    path('wawancara/', include('wawancara.urls', namespace='wawancara')),
    path('pembayaran/', include('pembayaran.urls', namespace='pembayaran')),
    path('pengumuman/', include('pengumuman.urls', namespace='pengumuman'))
]
