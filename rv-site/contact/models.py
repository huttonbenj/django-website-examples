from django.db import models
from phone_field import PhoneField
from pyuploadcare.dj.models import ImageField
import os


# Create your models here.
class Contact(models.Model):
    name = models.CharField(null=True, blank=False, max_length=100)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(null=True, blank=False, max_length=100)
    message = models.TextField(null=True, blank=False)

    class Meta:
        verbose_name = 'Inquiries'
        verbose_name_plural = 'Inquiries'

class Email(models.Model):
    reservation_number = models.CharField(null=True, blank=False, max_length=100)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(null=True, blank=False, max_length=100)
    coach_make = models.CharField(null=True, blank=False, max_length=100)
    coach_model = models.CharField(null=True, blank=False, max_length=100)
    coach_year = models.CharField(null=True, blank=False, max_length=100)
    coach_length = models.CharField(null=True, blank=False, max_length=100)
    trailer = models.BooleanField(null=True, blank=True)
    trailer_length = models.CharField(null=True, blank=True, max_length=100)
    pets = models.BooleanField(null=True, blank=True)
    pet_breed = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='../media/uploads')

    class Meta:
        verbose_name = 'RV Specs'
        verbose_name_plural = 'RV Specs'
