from django.db import models
from lots.models import Lot

from pyuploadcare.dj.models import ImageField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class LotForSale(models.Model):
    lot = models.ForeignKey(Lot, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=False, help_text="The sale price of the lot.")
    empty_lot = models.BooleanField(default=False, help_text="Check this if this is a bare lot that hasn't been built on yet.  Checking this will enable this lot to show the proper text, 'Lot for sale, $199,000.' on the lot-map popup preview when hovering.")
    pending_sale = models.BooleanField(default=False, help_text="Check this if the lot is pending sale.")

    def __str__(self):
        return f'Lot {self.lot.number}'

    class Meta:
        verbose_name = 'Lot For Sale Details'
        verbose_name_plural = 'Lot For Sale Details'

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

    def save(self, *args, **kwargs):
        existing_instance = Seo.objects.filter(main_page='ownership_feed')
        if existing_instance.exists():
            self.id = existing_instance.first().id
        super(Seo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'


class OwnerForms(models.Model):
    title = models.CharField(null=True, blank=False, max_length=50, help_text="Display title for the file.")
    file = models.FileField(null=True, blank=False, help_text="File to upload.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Owner Form'
        verbose_name_plural = 'Owner Forms'
