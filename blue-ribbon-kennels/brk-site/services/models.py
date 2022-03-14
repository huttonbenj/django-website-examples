from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import base
from sorl.thumbnail import get_thumbnail

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    description = RichTextField(null=True, blank=False)
    page_title_description = models.TextField(null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    slot_position = models.IntegerField(null=True, blank=False)

