"""rndm_number URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    path('', views.custom_login, name='main'),
    path('login/', views.auth, name='login'),
    path('rnd/', MainView.as_view(), name='rnd'),
    path('logout/', views.logout_view, name='logout'),

]

