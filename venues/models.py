from django.db import models

# Create your models here.


class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255)


    def __str__(self):
        return self.city_name



class Hotels(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    rating = models.FloatField()
    city = models.ForeignKey(city, on_delete=models.SET_NULL, null=True,blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class Halls(models.Model):
    hall_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True,blank=True)
    

    def __str__(self):
        return f"Hall: '{self.name}' hotel: '{self.hotel}' City: '{self.hotel.city}'"


