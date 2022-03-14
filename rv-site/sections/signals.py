# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver

# from .models import SeoHome, PageTitleHome

# from django.utils.html import strip_tags


# @receiver(pre_save, sender=PageTitleHome)
# def pre_save_pt(sender, instance, **kwargs):
#     if instance.description == None:
#         instance.description = ''
#     if instance.blog:
#         if instance.title == None or instance.title == '':
#             instance.title = instance.blog.title
#         if instance.description == None or instance.description == '':
#             instance.description = ' '.join(strip_tags(instance.blog.story).split('&nbsp;'))

# @receiver(post_save, sender=PageTitleHome)
# def post_save_pt(sender, instance, created, **kwargs):
#     if created:
#         if not instance.blog:
#             SeoHome(page_title=instance).save()


# @receiver(pre_save, sender=SeoHome)
# def pre_save_seob(sender, instance, **kwargs):
#     if instance.blog:
#         if instance.title == None or instance.title == '':
#             instance.title = instance.blog.title
#         if instance.description == None or instance.description == '':
#             instance.description = ' '.join(strip_tags(instance.blog.story).split('&nbsp;'))
#         if instance.slug == None or instance.slug == '':
#             instance.slug = '-'.join(instance.blog.title.split(' '))
        
#         if SeoHome.objects.filter(blog=instance.blog).exists():
#             SeoHome.objects.filter(blog=instance.blog).delete()
    
#     if not instance.blog and instance.page_title:
#         if instance.title == None or instance.title == '':
#             instance.title = instance.page_title.title
#         if instance.description == None or instance.description == '':
#             instance.description = ' '.join(strip_tags(instance.page_title.description).split('&nbsp;'))     
#         if instance.slug == None or instance.slug == '':
#             instance.slug = '-'.join(instance.title.split(' '))

#         if SeoHome.objects.filter(page_title=instance.page_title).exists():
#             SeoHome.objects.filter(page_title=instance.page_title).delete()
