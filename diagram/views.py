"""Views for diagram."""
import os
from django.shortcuts import render

from diagram import models 
from nautobot.dcim.models import Device, Site, Region
from django.conf import settings
from django.http import JsonResponse

def org_diagram_view(request):
    return render(request, "diagram/organization_diagram.html")

def device_diagram_view(request, pk):
    device = Device.objects.get(pk=pk)
    return render(request, "diagram/device_diagram.html", {"device": device, "pk": pk})

def load_org_data(request):
    if request.method == 'GET':
        response = {"name": "Organization",
                    "parent": "null",
                    "children": []
                    }
        i = 0
        for region in Region.objects.all():
            response["children"].append({
                "name": str(region.name),
                "parent": "Organization",
                "children": []
            })
            j = 0
            for site in Site.objects.filter(region=region).all():
                response["children"][i]["children"].append(
                    {
                        "name": str(site.name),
                        "parent": str(region.name),
                        "children": []
                    }
                )
                for device in Device.objects.filter(site=site).all():
                    response["children"][i]["children"][j]["children"].append(
                        {
                            "name": str(device.name),
                            "parent": str(site.name),
                            "children": []
                        }
                    )
                j += 1
            i += 1
        print(response)
        return JsonResponse(response, safe=False)

def load_hierachical_data(request, pk):
    if request.method == 'GET':
        device = Device.objects.get(pk=pk)
        region = device.site.region
        response = {"name": str(region.name),
                    "parent": "null",
                    "children": []
                    }
        i = 0
        for site in Site.objects.filter(region=region).all():
            response["children"].append({
                "name": str(site.name),
                "parent": "Organization",
                "children": []
            })
            for device in Device.objects.filter(site=site).all():
                response["children"][i]["children"].append(
                    {
                        "name": str(device.name),
                        "parent": str(site.name),
                        "children": []
                    }
                )
            i += 1
        return JsonResponse(response, safe=False)

