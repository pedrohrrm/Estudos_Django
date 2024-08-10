"""
URL configuration for projeto01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse

# por enquanto eu vou criar uma função e passar uma view

# HTTP Resquest


def my_view(request):
    return HttpResponse('Hello World!')
    # tem que retornar HTTP response


def my_sec_view(request):
    return HttpResponse('Essa é a homepage')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_sec_view),
    path('sobre/', my_view)
]
