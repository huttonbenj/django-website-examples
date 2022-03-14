from django.db import models
from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail

# Create your models here.
class FacilityPage(models.Model):
    page_title = models.CharField(max_length=255, null=True, blank=False)
    # page_title_image = models.ImageField(null=True, blank=False)
    # page_title_description = models.TextField(null=True, blank=False)
    content_title = models.CharField(max_length=255, null=True, blank=False)
    content_description = RichTextField(null=True, blank=False)
    content_image = models.ImageField(null=True, blank=False)

    # def save(self, *args, **kwargs):
    #     super(FacilityPage, self).save(*args, **kwargs)
    #     im = get_thumbnail(self.page_title_image, '1600', crop='smart', quality=100)
    #     self.page_title_image = f"/{'/'.join(im.url.split('/')[2:])}"
    #     super(FacilityPage, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Facility Page'

class Image(models.Model):
    facility_page = models.ForeignKey(FacilityPage, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)
