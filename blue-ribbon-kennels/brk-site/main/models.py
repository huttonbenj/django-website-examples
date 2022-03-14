from django.db import models

# Create your models here.
class Logo(models.Model):
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'