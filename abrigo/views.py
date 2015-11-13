from django.shortcuts import render
from abrigo.models import *
from django.http import HttpResponse
import logging
LOGGER=logging.getLogger(__name__)


def shelterDetail(request,place_id):
    
    obj=AbrigoLocation.objects.filter(location__place_id=place_id)[0]
    addresses_components = [] 
    for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
        types=[]
        for t in address_component.types.all():
            types.append(t.name.encode("utf-8"))

        addresses_components.append({
                "long_name": address_component.long_name,
                "short_name": address_component.short_name,                
                "types":types
                }
            )

    objJson = {
        "abrigo":obj.abrigo.nome,
        "address_components": addresses_components,
        "formatted_address": obj.location.formatted_address,
        "geometry": {
            "location": {
                "lat": obj.location.lat,
                "lng": obj.location.lng
                },
            "location_type": "ROOFTOP",
            "viewport": {
                "northeast": {
                    "lat": obj.location.viewport_northeast_lat,
                    "lng": obj.location.viewport_northeast_lng
                    },
                "southwest": {
                    "lat": obj.location.viewport_southwest_lat,
                    "lng": obj.location.viewport_southwest_lng
                    }
                },
            "bounds": {
                "northeast": {
                    "lat": obj.location.bound_northeast_lat,
                    "lng": obj.location.bound_northeast_lng
                    },
                "southwest": {
                    "lat": obj.location.bound_southwest_lat,
                    "lng": obj.location.bound_southwest_lng
                    }
                }
            },
        "place_id": str(obj.location.place_id),
        "types": [
            "street_address"
            ]
        }

    return HttpResponse("["+json.dumps(objJson).replace("'","\"")+"]")



def shelters(request):  
    arr=[]

   
    for abrigoLocation in AbrigoLocation.objects.all().distinct():
    
        obj= AbrigoLocation.objects.get(abrigo=abrigoLocation.abrigo)
        addresses_components = [] 
        for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
            types=[]
            for t in address_component.types.all():
                types.append(t.name.encode("utf-8")) 
                addresses_components.append({
                        "long_name": address_component.long_name.encode("utf-8"),
                        "short_name": address_component.short_name.encode("utf-8"),
                        "types": types
                        }
                                            )
        objJson = {
            "abrigo":abrigo.nome.encode("utf-8"),
            "address_components": addresses_components,
            "formatted_address": obj.location.formatted_address.encode("utf-8"),
            "geometry": {
                "location": {
                    "lat": obj.location.lat,
                    "lng": obj.location.lng
                    },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": obj.location.viewport_northeast_lat,
                        "lng": obj.location.viewport_northeast_lng
                        },
                    "southwest": {
                        "lat": obj.location.viewport_southwest_lat,
                        "lng": obj.location.viewport_southwest_lng
                        }
                    },
                "bounds": {
                    "northeast": {
                        "lat": obj.location.bound_northeast_lat,
                        "lng": obj.location.bound_northeast_lng
                        },
                    "southwest": {
                        "lat": obj.location.bound_southwest_lat,
                        "lng": obj.location.bound_southwest_lng
                        }
                    }
                },
            "place_id": str(obj.location.place_id),
            "types": [
                "street_address"
                ]
            }
        arr.append(objJson)              

    return HttpResponse(json.dumps(arr).replace("'","\""))


 
def shelterList(request,country_short_name):
    arr=[]
    LOGGER.error(country_short_name)
    locations_pk = AddressComponent.objects.filter(short_name=country_short_name).values_list('location__pk')
    LOGGER.error(locations_pk)
 
    for shelter  in AbrigoLocation.objects.filter(location__pk__in=locations_pk):
        LOGGER.error(shelter)
        arr.append(get_address(shelter)) 

    return HttpResponse(json.dumps(arr).replace("'","\""))

def get_address(obj):
    
    for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
        types=[]
        addresses_components=[]
        for t in address_component.types.all():
            types.append(t.name.encode("utf-8"))
            addresses_components.append({
                    "long_name": address_component.long_name.encode("utf-8"),
                    "short_name": address_component.short_name.encode("utf-8"), 
                    "types":types
                    }
                                        )

    objJson = {
        "abrigo":obj.abrigo.nome.encode("utf-8"),
        "address_components": addresses_components,
        "formatted_address": obj.location.formatted_address.encode("utf-8"),
        "geometry": {
            "location": {
                "lat": obj.location.lat,
                "lng": obj.location.lng
                },
            "location_type": "ROOFTOP",
            "viewport": {
                "northeast": {
                    "lat": obj.location.viewport_northeast_lat,
                    "lng": obj.location.viewport_northeast_lng
                    },
                "southwest": {
                    "lat": obj.location.viewport_southwest_lat,
                    "lng": obj.location.viewport_southwest_lng
                    }
                },
            "bounds": {
                "northeast": {
                    "lat": obj.location.bound_northeast_lat,
                    "lng": obj.location.bound_northeast_lng
                    },
                "southwest": {
                    "lat": obj.location.bound_southwest_lat,
                    "lng": obj.location.bound_southwest_lng
                    }
                }
            },
        "place_id": str(obj.location.place_id),
        "types": [
            "street_address"
            ]
        }

    return objJson
