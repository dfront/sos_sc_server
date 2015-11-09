from django.shortcuts import render
from abrigo.models import *
from django.http import HttpResponse

def getlocation(request,place_id):
    
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
  



def get(request):    
    arr=[]

    for abrigo in Abrigo.objects.all(): 
       obj= AbrigoLocation.objects.get(abrigo=abrigo)
       addresses_components =[] 
       for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
           types=[]
           for t in address_component.types.all():
               types.append(t.name.encode("utf-8"))
           
           addresses_components.append(
                {
                    "long_name": address_component.long_name.encode("utf-8"),
                    "short_name": address_component.short_name.encode("utf-8"),
                    "types": types
                    }
                )

       objJson = {
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
       arr.append(objJson)              
    
    return HttpResponse(json.dumps(arr).replace("'","\""))
  
