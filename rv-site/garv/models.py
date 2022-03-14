from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Garv(models.Model):
    rules = RichTextUploadingField(null=True, blank=False, help_text="Add most up to date GARV rules here.")

    class Meta:
        verbose_name = 'Rules'
        verbose_name_plural = 'Rules'

    def __str__(self):
        return 'Rules'