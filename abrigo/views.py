from django.shortcuts import render
from abrigo.models import *
from django.http import HttpResponse

def getlocation(request,slug):
    
    obj=AbrigoLocation.objects.filter(location__id=slug)[0]
    objJson = {
                "address_components": [
                    {
                        "long_name": str(obj.location.street_number),
                        "short_name": str(obj.location.street_number),
                        "types": [
                            "street_number"
                        ]
                    },
                    {
                        "long_name": str(obj.location.address_1),
                        "short_name": str(obj.location.address_1),
                        "types": [
                            "route"
                        ]
                    },
                    {
                        "long_name":  str(obj.location.address_2),
                        "short_name": str(obj.location.address_2),
                        "types": [
                            "locality",
                            "political"
                        ]
                    },
                    {
                        "long_name": str(obj.location.address_3),
                        "short_name": str(obj.location.address_3),
                        "types": [
                            "administrative_area_level_2",
                            "political"
                        ]
                    },
                    {
                        "long_name": str(obj.location.city),
                        "short_name": str(obj.location.city),
                        "types": [
                            "administrative_area_level_1",
                            "political"
                        ]
                    },
                    {
                        "long_name": str(obj.location.state),
                        "short_name": str(obj.location.state_short_name),
                        "types": [
                            "country",
                            "political"
                        ]
                    },
                    {
                        "long_name": str(obj.location.postcode),
                        "short_name": str(obj.location.postcode),
                        "types": [
                            "postal_code"
                        ]
                    }
                ],
                "formatted_address": str(obj.location.address_1),
                "geometry": {
                    "location": {
                        "lat": obj.location.latitude,
                        "lng": obj.location.longitude
                    },
                    "location_type": "ROOFTOP",
                    "viewport": {
                        "northeast": {
                            "lat": 0,
                            "lng": 0
                        },
                        "southwest": {
                            "lat": 0,
                            "lng": 0
                        }
                    }
                },
                "place_id": str(obj.location.pk),
                "types": [
                    "street_address"
                ]
            }
    return HttpResponse("["+json.dumps(objJson)+"]")

# Create your views here.
