"""
URL configuration for APIRD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from Drinks.views import home
from Drinks.views import get_drinks
from Drinks.views import add_drink
from Drinks.views import get_drink
from Drinks.views import update_drink
from Drinks.views import delete_drink



urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('',home ),
    path('get_drinks/', get_drinks),
    path('add_drink/', add_drink),
    path('get_drink/<int:id>/', get_drink),
    path('update_drink/<int:id>/', update_drink),
    path('delete_drink/<int:id>/', delete_drink),
]
