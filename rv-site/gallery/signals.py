from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Seo, PageTitle

from django.utils.html import strip_tags

@receiver(pre_save, sender=PageTitle)
def pre_save_gallery(sender, instance, **kwargs):
    if instance.description == None:
        instance.description = ''

@receiver(post_save, sender=PageTitle)
def post_save_pt_gallery(sender, instance, created, **kwargs):
    if created:
        Seo(page_title=instance).save()


@receiver(pre_save, sender=Seo)
def pre_save_seo_gallery(sender, instance, **kwargs):
    if instance.title == None or instance.title == '':
        instance.title = instance.page_title.title
    if instance.description == None or instance.description == '':
        instance.description = ' '.join(strip_tags(instance.page_title.description).split('&nbsp;'))     
    if instance.slug == None or instance.slug == '':
        instance.slug = '-'.join(instance.page_title.title.split(' '))
    instance.main_page = 'gallery'
