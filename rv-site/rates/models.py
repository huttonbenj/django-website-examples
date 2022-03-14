from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=25, choices=((u'1', 'Standard'), (u'2', 'Moderate'), (u'3', 'Deluxe'), (u'4', 'Luxury')), null=True, blank=False, help_text="The name of this package that will also be displayed as a title for this package's section of the web page.")
    description = models.TextField(null=True, blank=False, help_text="This description will be displayed directly under the name (title) of this package.")

    def __str__(self):
        return self.name

class Rate(models.Model):
    Package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=False)
    time_frame = models.CharField(max_length=25, choices=(('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')), null=True, blank=False, help_text="The timeframe that this rate applies to.")
    spring_summer_rate = models.IntegerField(null=True, blank=True, help_text="The rate for Spring/Summer for this timeframe.")
    fall_winter_rate = models.IntegerField(null=True, blank=True, help_text="The rate for Fall/Winter for this timeframe")
    call = models.BooleanField(default=False, help_text="If this is checked, no rates will be shown for this timeframe and the word 'CALL' will be displayed in the rate's place.  USE CASE: The Fall/Winter monthly rate for Luxury.")
    
    def __str__(self):
        return self.time_frame

class Detail(models.Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    detail = models.CharField(null=True, blank=True, max_length=255, help_text="The details are added below the rate as bullet points (just above the book now button for the rate).")

    def __str__(self):
        return self.detail

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
        existing_instance = Seo.objects.filter(main_page='rates')
        if existing_instance.exists():
            self.id = existing_instance.first().id
        super(Seo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

