from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class AboutPage(models.Model):
    page_title = models.CharField(max_length=255, null=True, blank=False)
    # page_title_description = models.TextField(null=True, blank=False)
    # page_title_image = models.ImageField(null=True, blank=False)
    what_we_do_image = models.ImageField(null=True, blank=False)
    who_we_are_title = models.CharField(max_length=255, null=True, blank=False)
    who_we_are_image = models.ImageField(null=True, blank=False)

    class Meta:
        verbose_name_plural = 'About Page'


class AboutTab(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=False)
    description = RichTextField(null=True, blank=False)
    order_num = models.IntegerField(null=True, blank=False)


class AboutAccordian(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    order_num = models.IntegerField(null=True, blank=False)


class TeamMember(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=False)
    job_title = models.CharField(max_length=255, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
