"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
""" Including another URLconf: urls.py trong folder cấu hình project"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# Ý nghĩa của cái file urls.py trong project
# Sau http://localhost:8000/ đọc cái gile myweb.urls.py
# DÙng để chia về các webapp.
# Dựa vào path/url 
urlpatterns = [
    path('api/', include('myapi.urls')),
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
]