"""djangoproject URL Configuration

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
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='home'),
    path('result1/', myapp.views.result1, name='result1'),
    path('result2/', myapp.views.result2, name='result2'),
    path('about1/', myapp.views.about1, name='about1'),
    path('about2/', myapp.views.about2, name='about2'),
    path('go1/', myapp.views.go1, name='go1'),
    path('go2/', myapp.views.go2, name='go2'),
]
