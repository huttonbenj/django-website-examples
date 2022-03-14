from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    # cart_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image_url = models.CharField(null=True, max_length=300)
    image_title = models.CharField(null=True, max_length=100)
    image_category = models.CharField(null=True, max_length=100)
    image_sub_category = models.CharField(null=True, max_length=100)
    image_price = models.CharField(null=True, max_length=20)
    image_description = models.TextField(null=True)


    class Meta:
        verbose_name_plural = 'Cart'

class CartBackground(models.Model):
    background_image = ImageField(null=True, help_text='Background image for the header of the Cart Checkout Page.')
    header_title = models.CharField(default='Shopping Cart', max_length=100, help_text='Title that is displayed over the background image.')

    class Meta:
        verbose_name_plural = 'Cart'
