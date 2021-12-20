"""Urls for diagram."""

from django.urls import path

from diagram import views

urlpatterns = [
    path("sites/ajax-data/", views.load_site_coordinates, name='load-sites'),
    path("org-map/", views.world_map_view, name='world-map-view'),
]