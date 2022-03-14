from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import AboutPage
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage 

# @receiver(pre_save, sender=AboutPage)
# def crop_and_resize_image(sender, instance, **kwargs):
#     pre_save.disconnect(crop_and_resize_image, sender=sender)

#     im = get_thumbnail(instance.page_title_image, '1600x700', crop='center', quality=100)
#     if not instance.id: 
#         fss = FileSystemStorage()
#         file = fss.save('thumb.jpg', ContentFile(im.read()))
#         file_url = fss.url(file)
#         instance.page_title_image = file_url.split('/')[-1]
#     else:
#         previous = sender.objects.get(id=instance.id)
#         if previous.page_title_image != instance.page_title_image: 
#             fss = FileSystemStorage()
#             file = fss.save('thumb.jpg', ContentFile(im.read()))
#             file_url = fss.url(file)
#             instance.page_title_image = file_url.split('/')[-1]

# @receiver(post_save, sender=AboutPage)
# def crop_and_resize_image(sender, instance, **kwargs):
#     pre_save.connect(crop_and_resize_image, sender=AboutPage)
