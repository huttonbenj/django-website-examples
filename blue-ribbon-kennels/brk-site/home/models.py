from django.db import models
from django.db.models.expressions import F

# Create your models here.


class Slide(models.Model):
    image = models.ImageField(null=True, blank=False)
    meta_title = models.CharField(max_length=255, null=True, blank=False)
    title = models.CharField(max_length=255, null=True, blank=False)
    description = models.CharField(max_length=255, null=True, blank=False)
    button_text = models.CharField(max_length=255, null=True, blank=False)
    button_link = models.CharField(max_length=255, null=True, blank=False)


class TestimonialSection(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    background_image = models.ImageField(null=True, blank=False)
    # button_text = models.CharField(max_length=25, null=True, blank=False)
    # button_url = models.URLField(null=True, blank=False)
    # fancy_item_1_label = models.CharField(max_length=25, null=True, blank=False)
    # fancy_item_1_count = models.IntegerField(null=True, blank=False)
    # fancy_item_2_label = models.CharField(max_length=25, null=True, blank=False)
    # fancy_item_2_count = models.IntegerField(null=True, blank=False)
    # fancy_item_3_label = models.CharField(max_length=25, null=True, blank=False)
    # fancy_item_3_count = models.IntegerField(null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Testimonial Section'

class Testimonial(models.Model):
    testimonial_section = models.ForeignKey(TestimonialSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=False)
    thumbnail = models.ImageField(null=True, blank=False)
    description = models.CharField(max_length=255, null=True, blank=False)
