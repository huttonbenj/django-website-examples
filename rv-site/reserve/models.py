from django.db import models
from pyuploadcare.dj.models import ImageField, FileField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Intro(models.Model):
    small_title = models.CharField(null=True, blank=False, max_length=255, verbose_name="Meta Title", help_text="This is displayed just above the main title at the top of the page and has smaller font.  It's meant to supplement the main title.")
    large_title = models.CharField(null=True, blank=False, max_length=255, verbose_name="Main Title", help_text="This is the main title for the page displayed at the top of the page just under the meta title.")
    description = RichTextUploadingField(null=True, blank=False, help_text="This is the description for the page displayed at the top just under the main title.")

    class Meta:
        verbose_name = 'Intro'
        verbose_name_plural = 'Intro'

class Rule(models.Model):
    icon = FileField(null=True, blank=False, help_text='Icon displayed in front of the rule (just for looks).')
    title = models.CharField(null=True, blank=False, max_length=255, help_text='This is the title of the rule which is what a visitor will see before clicking on the rule to expand it and see the description.')
    description = RichTextUploadingField(null=True, blank=False, help_text="This is the text a visitor will see after clicking on the rule and expanding it.")

    def __str__(self):
        return self.title

class WarningMessage(models.Model):
    message = RichTextUploadingField(null=True, blank=False, help_text="This warning message pops up at the bottom of the screen in order to warn users of the required RV specs.")


class Seo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, help_text="Enter SEO title.  This is not visible to visitors of the website and is strictly for SEO purposes.")
    description = models.TextField(null=True, blank=True, help_text="Enter SEO description.  This is not visible to visitors of the website and is strictly for SEO purposes.")
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="Leave blank to this the SEO title as the default.  Only letters, numbers, and hyphens can be used in the slug.  Cannot use special charaters or spaces (ex: can't use & or $).  If left blank to use the seo's title as the slug, it will remove special characters from the slug for you along with replacing the spaces with hyphens.", max_length=255)
    meta_tags = models.CharField(null=True, blank=True, max_length=510, help_text="Enter keywords separated by commas.  EX: word1, word2, word3  ***IMPORTANT: must separate by commas for it to help SEO***.")
    main_page = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

