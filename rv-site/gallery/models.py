from django.db import models
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Gallery(models.Model):
    image = ImageField(help_text='Image for the gallery.')
    title = models.CharField(null=True, blank=False, max_length=25, help_text='The title of the image.')
    category = models.CharField(null=True, blank=False, max_length=25, choices=(
        ('Lazy_River', 'Lazy River'),
        ('Indoor_Pool', 'Indoor Pool'),
        ('Clubhouse', 'Clubhouse'),
        ('Events', 'Events'),
        ('Resort', 'Resort'),
    ), help_text='The category of the image.')

    @classmethod
    def get_indices(cls, index, objs):
        start = 0
        stop = 5
        if index >= 5 and index % 5 == 0: 
            start = index
            stop = stop + 5
        if stop == len(objs)-1 and not start == 0:
            start = stop 
            stop = len(objs)
        return start, stop

    @classmethod
    def get_categories(cls):
        return {(s.category, s.get_category_display()) for s in cls.objects.all()}

    @classmethod
    def get_objs(cls):
        count = 0
        objs = list()
        for item in cls.objects.all():
            count +=1
            if count == 1:
                objs.append(('gallery/cycle1.html', item))
            if count == 2:
                objs.append(('gallery/cycle2.html', item))
            if count == 3:
                objs.append(('gallery/cycle3.html', item))
            if count == 4:
                objs.append(('gallery/cycle4.html', item))
            if count == 5:
                objs.append(('gallery/cycle5.html', item))
                count = 0
        return objs

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

class PageTitle(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, help_text='The title displayed at the top of the page.')
    description = models.CharField(null=True, blank=True, max_length=255, help_text='The description displayed at the top of the page under the title.')
    background_image = ImageField(blank=True, help_text='The image displayed at the top of the page.  The title and description overlay this image.')

    class Meta:
        verbose_name = 'Page Title/SEO'
        verbose_name_plural = 'Page Title/SEO'

class Seo(models.Model):
    page_title = models.ForeignKey(PageTitle, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=255, help_text="Leave blank to use this page's title as the default.  This is not visible to visitors of the website and is strictly for SEO purposes.")
    description = models.TextField(null=True, blank=True, help_text="Leave blank to use this page's description as the default.  This is not visible to visitors of the website and is strictly for SEO purposes.")
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="Leave blank to this the page's title as the default.  Only letters, numbers, and hyphens can be used in the slug.  Cannot use special charaters or spaces (ex: can't use & or $).  If left blank to use the page's title as the slug, it will remove special characters from the slug for you along with replacing the spaces with hyphens.", max_length=255)
    main_page = models.CharField(null=True, blank=True, max_length=255)
    meta_tags = models.CharField(null=True, blank=True, max_length=510, help_text="Enter keywords separated by commas.  EX: word1, word2, word3  ***IMPORTANT: must separate by commas for it to help SEO***.")

    def save(self, *args, **kwargs):
        existing_instance = Seo.objects.filter(main_page='gallery')
        if existing_instance.exists():
            self.id = existing_instance.first().id
        super(Seo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'
