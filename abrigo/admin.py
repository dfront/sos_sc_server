from django.contrib import admin
from abrigo.models import *
from django.http import HttpResponse
from django.core import serializers
import json
from django.contrib.contenttypes.models import ContentType

def makeJSON(modeladmin,request,queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    handle1=open('/var/projetos/sos_server/static/json/abrigos_template.json','w+')
    arr=[]
    for obj in AbrigoLocation.objects.filter(abrigo_id__in=selected):       
        addresses_components =[] 
        for address_component in AddressComponent.objects.filter(location__pk=obj.location.pk):
            addresses_components.append(
                {
                    "long_name": address_component.long_name,
                    "short_name": address_component.short_name,
                    "types": address_component.types
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
    
    handle1.write("["+str(','.join(map(str,arr))).replace("'","\"")+"]")
    handle1.close()

makeJSON.short_description = "Gerar JSON"



class AddressComponentAdmin(admin.ModelAdmin):
    def types(self):        
        return (self.types.all().values_list('name'))
    list_display = ('pk','short_name','long_name','location',types) 
    
class AbrigoInline(admin.TabularInline):
    model = Abrigo

class LocationInline(admin.TabularInline):
    model= AbrigoLocation

class AbrigoAdmin(admin.ModelAdmin):
    list_display = ('pk','nome')
    actions = [makeJSON]
    inlines = [LocationInline]
  

class AddressComponentInline(admin.TabularInline):
    model=AddressComponent

class LocationAdmin(admin.ModelAdmin):
    inlines = [AddressComponentInline]
   


admin.site.register(Abrigo,AbrigoAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(AddressComponent,AddressComponentAdmin)
admin.site.register(AddressComponentType)
