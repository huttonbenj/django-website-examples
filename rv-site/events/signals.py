from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Event, Seo, PageTitle

from django.utils.html import strip_tags

def create_slug(title):
    cleaned = str()
    for char in title:
        if char.isalnum():
            cleaned += char
        if char.isspace() and not cleaned[-1] == '-':
            cleaned += '-'
    return cleaned


@receiver(post_save, sender=Event)
def post_save_event(sender, instance, created, **kwargs):
    page_title = PageTitle.objects.get_or_create(event=instance)
    seo = Seo.objects.get_or_create(event=instance)


@receiver(pre_save, sender=PageTitle)
def pre_save_pt_event(sender, instance, **kwargs):

    if sender.objects.filter(event=instance.event).exists():
        instance.id = sender.objects.filter(event=instance.event).first().id

    if instance.event:
        if not instance.title:
            instance.title = instance.event.short_title
        if not instance.background_image:
            instance.background_image = instance.event.background_image


@receiver(pre_save, sender=Seo)
def pre_save_seo_event(sender, instance, **kwargs):

    if sender.objects.filter(event=instance.event).exists():
        instance.id = sender.objects.filter(event=instance.event).first().id
    
    if instance.event:
        if not instance.title:
            instance.title = instance.event.short_title
        if not instance.description:
            instance.description = strip_tags(instance.event.description)
        if not instance.slug:
            instance.slug = create_slug(instance.event.short_title)

