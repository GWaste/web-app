from django.contrib import admin
from django.urls import include, path

import webapp.views

urlpatterns = [
    path('', webapp.views.home, name='home'),
    path('camera', webapp.views.camera, name='camera'),
    path('predict', webapp.views.predict, name='predict'),
    path('favorites', webapp.views.favorites, name='favorites'),
]