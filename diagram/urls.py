"""Urls for diagram."""

from django.urls import path

from diagram import views

urlpatterns = [
    path("org-diagram/", views.OrgDiagramView.as_view(), name='org-diagram'),
    path("org-diagram/ajax-data/", views.load_org_data, name='load-org-data'),
    path("devices/<uuid:pk>/diagram/", views.DeviceDiagramView.as_view(), name='device-diagram-view'),
    path("devices/<uuid:pk>/ajax-data/", views.load_device_data, name='load-data'),
]