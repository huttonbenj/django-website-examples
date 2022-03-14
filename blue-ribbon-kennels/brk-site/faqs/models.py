from django.db import models
from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail

# Create your models here.
class FaqPage(models.Model):
    page_title = models.CharField(max_length=255, null=True, blank=False)
    # page_title_image = models.ImageField(null=True, blank=False)
    # page_title_description = models.TextField(null=True, blank=False)

    # def save(self, *args, **kwargs):
    #     super(FaqPage, self).save(*args, **kwargs)
    #     im = get_thumbnail(self.page_title_image, '1600', crop='smart', quality=100)
    #     self.page_title_image = f"/{'/'.join(im.url.split('/')[2:])}"
    #     super(FaqPage, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Faq Page'

class AccordionEntry(models.Model):
    faq_page = models.ForeignKey(FaqPage, on_delete=models.CASCADE)
    icon = models.FileField(null=True, blank=False, help_text="Upload an .svg (icon) to be displayed for this FAQ.  This is located just left of the FAQ's title.")
    title = models.CharField(max_length=255, null=True, blank=False)
    description = RichTextField(null=True, blank=False)
    order_num = models.IntegerField(null=True, blank=False)
