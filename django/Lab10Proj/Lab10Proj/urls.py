"""
URL configuration for Lab10Proj project.

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
from TestApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/', views.person_list.as_view(), name='person-list'),
    path('students/', views.student_list.as_view(), name='studnet-list'),
    path('teachers/', views.teacher_list.as_view(), name='teacher-list'),
]
