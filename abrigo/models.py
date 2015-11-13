from django.db import models
import json, urllib
from django.db.models import signals


class Abrigo(models.Model):
    nome = models.CharField(max_length=255)


    def getLocationsByCountry(self,country_short_name):        
        return AddressComponent.objects.filter(short_name=country_short_name).values_list('locations')
   
    def locations(self): 
        return AbrigoLocation.objects.filter(abrigo=self).values('locations')

    def __unicode__(self):
        return self.nome

def getLatLon(address):
    address = urllib.quote_plus(address)
    geo = urllib.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=%s" % (address))
    return geo.read()

class Location(models.Model):   
    place_id = models.CharField(max_length=200, blank=True, null=True) 
    formatted_address = models.CharField(max_length=200, blank=True, null=True)
    #geometry
    lat = models.CharField(max_length=50, blank=True, null=True)
    lng = models.CharField(max_length=50, blank=True, null=True)
    bound_northeast_lat = models.CharField(max_length=50, blank=True, null=True)
    bound_northeast_lng = models.CharField(max_length=50, blank=True, null=True)
    bound_southwest_lat = models.CharField(max_length=50, blank=True, null=True)
    bound_southwest_lng = models.CharField(max_length=50, blank=True, null=True)
    viewport_southwest_lat = models.CharField(max_length=50, blank=True, null=True)
    viewport_southwest_lng = models.CharField(max_length=50, blank=True, null=True)
    viewport_northeast_lat = models.CharField(max_length=50, blank=True, null=True)
    viewport_northeast_lng = models.CharField(max_length=50, blank=True, null=True)   

    location_type = models.CharField(max_length=100, blank=True, null=True)

    def save(self):
        geo = json.loads(getLatLon("%s" % (self.formatted_address.encode("utf-8"))))
        if geo['status'] == "OK":
            self.place_id = geo['results'][0]['place_id']
            self.formatted_address = geo['results'][0]['formatted_address']
            self.lat = geo['results'][0]['geometry']['location']['lat']
            self.lng = geo['results'][0]['geometry']['location']['lng']
            if 'bounds' in geo['results'][0]['geometry']:
                self.bound_northeast_lat = geo['results'][0]['geometry']['bounds']['northeast']['lat']
                self.bound_northeast_lng = geo['results'][0]['geometry']['bounds']['northeast']['lng']
                self.bound_southwest_lat = geo['results'][0]['geometry']['bounds']['southwest']['lat']
                self.bound_southwest_lng = geo['results'][0]['geometry']['bounds']['southwest']['lng']

            self.viewport_northeast_lat = geo['results'][0]['geometry']['viewport']['northeast']['lat']
            self.viewport_northeast_lng = geo['results'][0]['geometry']['viewport']['northeast']['lng']
            self.viewport_southwest_lat = geo['results'][0]['geometry']['viewport']['southwest']['lat']
            self.viewport_southwest_lng = geo['results'][0]['geometry']['viewport']['southwest']['lng']
            self.location_type = geo['results'][0]['geometry']['location_type']
            super(Location,self).save()


    def addresses_components(self):
        return AddressComponent.objects.filter(location=self)

    def __unicode__(self):
        return self.formatted_address


class AddressComponentType(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

class AddressComponent(models.Model):
   # pk = models.IntegerField(max_length=10,primary_key=True)
    types = models.ManyToManyField(AddressComponentType)
    long_name = models.CharField(max_length=200, blank=True, null=True)
    short_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.short_name

class AbrigoLocation(models.Model):
    #pk = models.IntegerField(max_length=5,primary_key=True)
    abrigo = models.ForeignKey(Abrigo)
    location = models.ForeignKey(Location)

    
  


def post_save_location(sender,instance, **kwargs):
    geo = json.loads(getLatLon("%s" % (instance.formatted_address.encode("utf-8"))))
    if geo['status'] == "OK":           
        address_components = geo['results'][0]['address_components']
    
        for ad in address_components:
            types=[]          
        
            long_name=ad["long_name"]
            short_name=ad["short_name"]
        
            for type_ in ad["types"]:
                obj, created=AddressComponentType.objects.get_or_create(name=type_,defaults={"name":type_})
                types.append(obj)                    
                
                
            ad,created=AddressComponent.objects.get_or_create(location=instance,long_name=long_name,short_name=short_name,defaults={"long_name":long_name,"short_name":short_name,"location":instance})
            ad.types=types
            ad.save()       

signals.post_save.connect(post_save_location, sender=Location)
