from django.contrib import admin
from django.urls import include, path

import webapp.views

urlpatterns = [
    path('', webapp.views.home)
]