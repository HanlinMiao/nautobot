"""Views for diagram."""

from django.shortcuts import render
# from django.views.generic import views

from diagram import models

def diagram_view(request):
    return render(request, "diagram/device_diagram.html")
