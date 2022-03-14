from django.db import models
from pyuploadcare.dj.models import ImageField, FileField
from ckeditor_uploader.fields import RichTextUploadingField
from rates.models import Package


# Create your models here.
class Lot(models.Model):
    number = models.IntegerField(null=True, blank=False, unique=True, help_text="This will be used as the title at the top of this lot's page.  EX: It will be displayed as, 'Lot 12'")
    description = RichTextUploadingField(null=True, blank=False, help_text="This is the main description of the lot.  It is displayed directly below the photos of the lot on this lot's page.")
    package = models.CharField(null=True, blank=False, max_length=25, choices=(
        ('standard', 'Standard'),
        ('moderate', 'Moderate'),
        ('deluxe', 'Deluxe'),
        ('luxury', 'Luxury'),
    ), help_text="The package of this lot will be displayed on the lot's page and on the popup preview on the lot-map.")

    def __str__(self):
        return f'Lot {self.number}'

class Image(models.Model):
    lot = models.ForeignKey(Lot, null=True, blank=False, on_delete=models.CASCADE)
    image = ImageField(help_text="Upload images for the lot to be displayed on the lot's page.  Note: The first image uploaded for this lot will be the image that is used for the lot-map popup preview image.")

class Features(models.Model):
    lot = models.ForeignKey(Lot, null=True, blank=False, on_delete=models.CASCADE)
    label = models.CharField(null=True, blank=False, max_length=25, verbose_name="Feature", help_text="Features are displayed under the description of the lot on the lot's page.  EX: WIFI")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

class PageTitle(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, help_text='The title displayed at the top of the page.')
    description = models.CharField(null=True, blank=True, max_length=255, help_text='The description displayed at the top of the page under the title.')
    background_image = ImageField(blank=True, help_text='The image displayed at the top of the page.  The title and description overlay this image.')

    class Meta:
        verbose_name = 'Page Title/SEO'
        verbose_name_plural = 'Page Title/SEO'


class Seo(models.Model):
    page_title = models.ForeignKey(PageTitle, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=255, help_text="Leave blank to use this page's title as the default.  This is not visible to visitors of the website and is strictly for SEO purposes.")
    description = models.TextField(null=True, blank=True, help_text="Leave blank to use this page's description as the default.  This is not visible to visitors of the website and is strictly for SEO purposes.")
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="Leave blank to this the page's title as the default.  Only letters, numbers, and hyphens can be used in the slug.  Cannot use special charaters or spaces (ex: can't use & or $).  If left blank to use the page's title as the slug, it will remove special characters from the slug for you along with replacing the spaces with hyphens.", max_length=255)
    meta_tags = models.CharField(null=True, blank=True, max_length=510, help_text="Enter keywords separated by commas.  EX: word1, word2, word3  ***IMPORTANT: must separate by commas for it to help SEO***.")
    main_page = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'
