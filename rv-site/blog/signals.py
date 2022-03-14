from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
from django.dispatch import receiver

from .models import Blog, Seo, PageTitle

from django.utils.html import strip_tags

def create_slug(title):
    cleaned = str()
    for char in title:
        if char.isalnum():
            cleaned += char
        if char.isspace() and not cleaned[-1] == '-':
            cleaned += '-'
    return cleaned


@receiver(post_save, sender=Blog)
def post_save_blog(sender, instance, created, **kwargs):
    page_title = PageTitle.objects.get_or_create(blog=instance)
    seo = Seo.objects.get_or_create(blog=instance)


@receiver(pre_save, sender=PageTitle)
def pre_save_pt_blog(sender, instance, **kwargs):

    if sender.objects.filter(blog=instance.blog).exists():
        instance.id = sender.objects.filter(blog=instance.blog).first().id

    if instance.blog:
        if not instance.title:
            instance.title = instance.blog.title
        if not instance.background_image:
            instance.background_image = Seo.objects.filter(main_page='blog_feed').last().page_title.background_image


@receiver(pre_save, sender=Seo)
def pre_save_seo_blog(sender, instance, **kwargs):

    if sender.objects.filter(blog=instance.blog).exists():
        instance.id = sender.objects.filter(blog=instance.blog).first().id
    
    if instance.blog:
        if not instance.title:
            instance.title = instance.blog.title
        if not instance.description:
            instance.description = strip_tags(instance.blog.story)
        if not instance.slug:
            instance.slug = create_slug(instance.blog.title)
