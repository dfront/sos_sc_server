from django.db import models
import json, urllib


class Abrigo(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome

def getLatLon(address):
    address = urllib.quote_plus(address)
    geo = urllib.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=%s" % (address))
    return geo.read()

class Location(models.Model):   
    place_id = models.CharField(max_length=200, blank=True, null=True)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    address_3 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)    
    state = models.CharField(max_length=200, blank=True, null=True)
    state_short_name = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=15,blank=True, null=True)
    street_number = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __unicode__(self):
        return self.address_1

    def save(self, *args, **kwargs):
        geo = json.loads(getLatLon("%s,%s,%s,%s %s" % (self.address_1, self.address_2, self.address_3, self.city, self.postcode)))
        if geo['status'] == "OK":
            self.latitude = geo['results'][0]['geometry']['location']['lat']
            self.longitude = geo['results'][0]['geometry']['location']['lng']
       
        super(Location, self).save(*args, **kwargs)


class AbrigoLocation(models.Model):
    abrigo = models.ForeignKey(Abrigo)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.abrigo.nome
