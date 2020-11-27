from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
        path('',views.Home,name='home'),
        path('sighup/',views.Sighup,name='sighup'),
        path('sighup/sighin/',views.Sighin,name='sighin'),


]
