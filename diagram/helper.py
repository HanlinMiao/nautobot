import uuid
from nautobot.dcim.models import Device, Site, Region, Rack, RackGroup, DeviceRole

def convert_js_to_python(js_array, id=False):
    js_array = js_array[1:len(js_array)-1].split(", ")
    py_array = []
    if js_array == ['']:
        return []
    if not id:
        for entry in js_array:
            py_array.append(entry[6:len(entry)-6])
        return py_array
    else:
        for entry in js_array:
            print(entry)
            print(entry[6:len(entry)-6])
            py_array.append(uuid.UUID(entry[6:len(entry)-6]).hex)
        return py_array

def query_org_data(region=[], site=[], group=[], rack=[], role=[], status=[], type=[]):
    if region:
        regions = Region.objects.filter(slug__in=region)
    else:
        regions = Region.objects.all()
    if site:
        sites = Site.objects.filter(slug__in=site)
    else:
        sites = Site.objects.all()
    if group:
        groups = RackGroup.objects.filter(pk__in=group)
    else:
        groups = RackGroup.objects.all()
    if rack:
        racks = Rack.objects.filter(pk__in=rack)
    else:
        racks = Rack.objects.all()
    if role:
        devices = Device.objects.filter(device_role__slug__in=role)
    else:
        devices = Device.objects.all()
    if status:
        devices = devices.filter(status__slug__in=status)
    else:
        devices = devices
    if type:
        devices = devices.filter(device_type__in=type)
    else:
        devices = devices

    response = {"name": "Organization",
                "parent": "null",
                "children": []
                }
    i = 0
    for region in regions:
        response["children"].append({
            "name": str(region.name),
            "parent": "Organization",
            "children": []
        })
        j = 0
        for site in sites.filter(region=region).all():
            response["children"][i]["children"].append(
                {
                    "name": str(site.name),
                    "parent": str(region.name),
                    "children": []
                }
            )
            k = 0
            for group in groups.filter(site=site).all():
                response["children"][i]["children"][j]["children"].append(
                {
                    "name": str(group.name),
                    "parent": str(site.name),
                    "children": []
                }
            )   
                x = 0
                for rack in racks.filter(group=group).all():
                    response["children"][i]["children"][j]["children"][k]["children"].append(
                        {
                            "name": str(rack.name),
                            "parent": str(group.name),
                            "children": []
                        }
                    )
                    for device in devices.filter(rack=rack).all():
                        response["children"][i]["children"][j]["children"][k]["children"][x]["children"].append(
                        {
                            "name": str(device.name),
                            "parent": str(rack.name),
                            "children": []
                        }
                    )
                    x += 1
                k += 1
            j += 1
        i += 1
    
    return response


def query_hierachical_data(region):
    response = {"name": str(region.name),
                "parent": "null",
                "children": []
                }
    j = 0
    for site in Site.objects.filter(region=region).all():
        response["children"].append(
            {
                "name": str(site.name),
                "parent": str(region.name),
                "children": []
            }
        )
        k = 0
        for group in RackGroup.objects.filter(site=site).all():
            response["children"][j]["children"].append(
            {
                "name": str(group.name),
                "parent": str(site.name),
                "children": []
            }
        )   
            x = 0
            for rack in Rack.objects.filter(group=group).all():
                response["children"][j]["children"][k]["children"].append(
                    {
                        "name": str(rack.name),
                        "parent": str(group.name),
                        "children": []
                    }
                )
                for device in Device.objects.filter(rack=rack).all():
                    response["children"][j]["children"][k]["children"][x]["children"].append(
                    {
                        "name": str(device.name),
                        "parent": str(rack.name),
                        "children": []
                    }
                )
                x += 1
            k += 1
        j += 1
    
    return response