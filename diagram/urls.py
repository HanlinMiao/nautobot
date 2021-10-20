"""Urls for diagram."""

from django.urls import path

from diagram import views

urlpatterns = [
    path("org-diagram/", views.org_diagram_view, name='org-diagram'),
    path("org-diagram/ajax-data/", views.load_org_data, name='load-org-data'),
    path("devices/<uuid:pk>/diagram/", views.device_diagram_view, name='device-diagram-view'),
    path("devices/<uuid:pk>/ajax-data/", views.load_hierachical_data, name='load-data'),
]