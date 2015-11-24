# -*- coding: utf-8 -*-
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
    addresses_components=[]
    list_state=[]
    for obj in AbrigoLocation.objects.all():               
        types=[]
        for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
            address_component_type = AddressComponentType.objects.filter(name__contains='administrative_area_level_1')[0]
            if  address_component_type not in address_component.types.all():
                continue


            if address_component.short_name in list_state:
                continue
        
            list_state.append(address_component.short_name)

            types.append(address_component_type.name.encode("utf-8"))
            addresses_components.append({
                    "long_name": address_component.long_name.encode("utf-8"),
                    "short_name":address_component.short_name.encode("utf-8"),
                    "types": types
                    })

    return HttpResponse(json.dumps(addresses_components).replace("'","\""))

def nearbyPoints(request,latlong):
    arr=[]
    #    locations_pk = AddressComponent.objects.filter(short_name=country_short_name).values_list('location__pk')
  #  LOGGER.error(locations_pk)
    


    for shelter in AbrigoLocation.objects.raw("SELECT * FROM abrigo_abrigolocation WHERE abrigo_id IN (SELECT id FROM abrigo_abrigo WHERE id IN (SELECT abrigo_id FROM abrigo_abrigolocation WHERE location_ID IN (SELECT id FROM abrigo_location WHERE (ABS(bound_northeast_lng - bound_southwest_lng) < 20) AND (ABS(bound_northeast_lat - bound_southwest_lat) < 20))))"):
        LOGGER.error(shelter)
        arr.append(get_address(shelter)) 

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
    addresses_components=[]
    for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
        types=[]

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
