"""Urls for diagram."""

from django.urls import path

from diagram import views

urlpatterns = [
    path("device-diagram/", views.diagram_view, name='device-diagram'),
]