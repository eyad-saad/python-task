"""server URL Configuration

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
from django.contrib import admin
from django.urls import path

from subscriber.views import HandleMessage, MaxTemperature, DataPointCount, MaxTemperaturePerDay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events', HandleMessage.as_view()),
    path('data-point/max-temperature', MaxTemperature.as_view()),
    path('data-point/count', DataPointCount.as_view()),
    path('data-point/max-temperature-per-day', MaxTemperaturePerDay.as_view()),

]
