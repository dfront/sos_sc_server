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
        arr.append(objJson)
        
       
    
    handle1.write("["+str(','.join(map(str,arr))).replace("'","\"")+"]")
    handle1.close()

makeJSON.short_description = "Gerar JSON"



class AbrigoLocationInline(admin.TabularInline):
    model = AbrigoLocation
    extra = 1

class AbrigoAdmin(admin.ModelAdmin):
    list_display = ('pk','nome')
    inlines = [AbrigoLocationInline,]
    actions = [makeJSON]

admin.site.register(Abrigo,AbrigoAdmin)
admin.site.register(Location)
