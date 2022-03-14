from django.db import models

CATEGORIES = (
    ('obedience', 'Obedience Training'),
    ('retriever', 'Retriever Training'),
    ('facility', 'Facility'),
)


class GalleryPage(models.Model):
    page_title = models.CharField(max_length=255, null=True, blank=False)
    # page_title_image = models.ImageField(null=True, blank=False)
    # page_title_description = models.TextField(null=True, blank=False)
    
    class Meta:
        verbose_name_plural = 'Gallery Page'

class Image(models.Model):
    gallery_page = models.ForeignKey(GalleryPage, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORIES, null=True, blank=False)

    @classmethod
    def get_category_filters(cls):
        return set([cat[0] for cat in CATEGORIES])

        