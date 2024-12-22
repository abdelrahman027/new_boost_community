from datetime import date
from ssl import create_default_context
from django.utils import timezone
from django.db import models


# from base.models import Course



# Create your models here.


class Trainer_hotel_payment_status(models.TextChoices):
    pending="Pending"
    paid="Paid"


class Visa_status(models.TextChoices):
    applied="Applied"
    processing="Processing"
    issued="Issued"




class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50 ,default="example@email.com")
    nationality = models.CharField(max_length=255)
    residence_location=models.CharField(max_length=255)
    field_of_experties=models.CharField(max_length=255)
    average_rate = models.CharField(max_length=20)
    trainer_category = models.CharField(max_length=20)
    cv = models.FileField(null=True,blank=True,upload_to='pdf')
    linkedin=models.CharField(blank=True,null=True, max_length=255)
    trainer_photo= models.ImageField(upload_to='trainers/', default='employee_photos/avatar.png', null=True, blank=True)
    passport_scan = models.FileField(null=True,blank=True,upload_to='pdf')
    bank_account_number=models.CharField(max_length=500,null=True,blank=True)
    bank_swift_code=models.CharField(max_length=500,null=True,blank=True)
    account_currency=models.CharField(max_length=20,null=True,blank=True)
    account_branch=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
    



class Trainers_hotel(models.Model):
    hotel_id=models.AutoField(primary_key=True)
    hotel_name=models.CharField(max_length=255)
    hotel_location=models.CharField(max_length=255)
    number_of_night=models.CharField(max_length=2)
    reservation_date=models.DateField(auto_now_add=True)
    payment_status=models.CharField(max_length=255,choices=Trainer_hotel_payment_status.choices)
    trainer= models.ForeignKey(Trainer,on_delete=models.CASCADE)
    # course =models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trainer}  hotel: {self.hotel_name}"
    


class Flight(models.Model):
    flight_id=models.AutoField(primary_key=True)
    trainer= models.ForeignKey(Trainer,on_delete=models.CASCADE)
    # course =models.ForeignKey(Course,on_delete=models.CASCADE)
    departure_date=models.DateTimeField(null=True,blank=True)
    flight_from=models.CharField(max_length=255,default="Cairo")
    flight_to=models.CharField(max_length=255,default="Abudhabi")
    Ticket= models.FileField(null=True,blank=True,upload_to='pdf')
    created_at= models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.trainer} hotel: {self.flight_id}"
    


class Visa(models.Model):
    visa_id=models.AutoField(primary_key=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    # course=models.ForeignKey(Course,on_delete=models.CASCADE)
    country=models.CharField(max_length=255)
    status=models.CharField(max_length=100,choices=Visa_status.choices)
    vis_pdf=models.FileField(null=True,blank=True,upload_to='pdf')
    created_at= models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.trainer} country: {self.country}"

