"""Views for diagram."""
import os
from django.shortcuts import render
from diagram import models 
from diagram.helper import query_org_data, convert_js_to_python, query_hierachical_data
from nautobot.dcim.models import Device, Site, Region
from django.conf import settings
from django.http import JsonResponse
from nautobot.core.views import generic
from nautobot.dcim import filters, forms, tables

def load_org_data(request):
    if request.method == 'GET':
        region = convert_js_to_python(request.GET.get("region"))
        site = convert_js_to_python(request.GET.get("site"))
        role = convert_js_to_python(request.GET.get("role"))
        status = convert_js_to_python(request.GET.get("status"))
        group = convert_js_to_python(request.GET.get("group"), id=True)
        type = convert_js_to_python(request.GET.get("type"), id=True)
        rack = convert_js_to_python(request.GET.get("rack"), id=True)

        response = query_org_data(region=region, site=site, group=group, rack=rack, role=role, status=status, type=type)

        return JsonResponse(response, safe=False)

def load_device_data(request, pk):
    if request.method == 'GET':
        device = Device.objects.get(pk=pk)
        region = device.site.region
        response = query_hierachical_data(region=region)

        return JsonResponse(response, safe=False)

class DeviceDiagramView(generic.ObjectView):
    queryset = Device.objects.all()
    filterset = filters.DeviceFilterSet
    filterset_form = forms.DeviceFilterForm
    template_name = "diagram/device_diagram.html"

    def get(self, request, pk):
        device = Device.objects.get(pk=pk)
        region = device.site.region
        site = device.site
        group = device.rack.group
        type = device.device_type
        rack = device.rack
        context = {
            "device": device,
            "region": region,
            "site": site,
            # "role": role,
            # "status": status,
            "group": group,
            "type": type,
            "rack": rack,
            "filter_form": self.filterset_form(request.GET, label_suffix="")  # pylint: disable=W0125
            if self.filterset_form
            else None,
        }
        return render(request, self.template_name, context)

class OrgDiagramView(generic.ObjectListView):
    queryset = Device.objects.all()
    filterset = filters.DeviceFilterSet
    filterset_form = forms.DeviceFilterForm
    template_name = "diagram/organization_diagram.html"

    def get(self, request):
        region = request.GET.getlist("region")
        site = request.GET.getlist("site")
        role = request.GET.getlist("role")
        status = request.GET.getlist("status")
        group = request.GET.getlist("rack_group_id")
        type = request.GET.getlist("device_type_id")
        rack = request.GET.getlist("rack_id")
        context = {
            "region": region,
            "site": site,
            "role": role,
            "status": status,
            "group": group,
            "type": type,
            "rack": rack,
            "filter_form": self.filterset_form(request.GET, label_suffix="")  # pylint: disable=W0125
            if self.filterset_form
            else None,
        }
        return render(request, self.template_name, context)

def device_diagram_view(request, pk):
    device = Device.objects.get(pk=pk)
    return render(request, "diagram/device_diagram.html", {"device": device, "pk": pk})

