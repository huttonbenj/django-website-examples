from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Event(models.Model):
    event_type = models.CharField(null=True, blank=False, max_length=25, choices=(('guest_event', 'Guest Event'), ('owner_event', 'Owner Event')), verbose_name='Type', help_text="This is shown on the event feed page next to each event's title to let people know whether guest can come or if it's an owners only")
    short_title = models.CharField(null=True, blank=False, max_length=50, verbose_name='title', help_text='The title for the event.  Shown both on the event feed page and on the individual event post page.')
    background_image = models.ImageField(null=True, blank=False, verbose_name='image', help_text="This is the image for the event.  Shown on botht the event feed page and individual event post page.")
    datetime = models.DateTimeField(null=True, verbose_name="Date/Time of Event", help_text='Date/Time of the event.  Only events with future dates will be visible to visitors on the website.')
    location = models.CharField(null=True, blank=False, max_length=255, help_text='Physical location of the event.')
    description = RichTextUploadingField(null=True, blank=False, help_text='This is partially shown on the event feed page depending on the length.  The full description can be seen on the indivdual event post page.')

    def __str__(self):
        return self.short_title


class PageTitle(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=255, help_text="FOR EVENT POST: leave blank to use the event's title as the default.  FOR EVENT FEED: must enter value.  This is shown at the top of the page.")
    description = models.CharField(null=True, blank=True, max_length=255, help_text="The description is directly under the page title at the top of the page.  This has no default so you must fill this out if you want a description to display.  Leave blank for no description.")
    background_image = models.ImageField(null=True, blank=True, help_text="FOR EVENT POST: leave blank to use the event's image as the default.  FOR EVENT FEED: must enter value.  This is shown at the top of the page.")

    class Meta:
        verbose_name = 'Page Title/SEO'
        verbose_name_plural = 'Page Title/SEO'


class Seo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    page_title = models.ForeignKey(PageTitle, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=255, help_text="FOR EVENT POSTS: leave blank to use the event's title as the default.  FOR EVENT FEED: must enter a value.  This is used for SEO purposes and is not visible to users anywhere on the website.")
    description = models.TextField(null=True, blank=True, help_text="FOR EVENT POSTS: leave blank to use the event's description as the default.  FOR EVENT FEED: must enter a value.  This is used for SEO purposes and is not visible to users anywhere on the website.")
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="Leave blank to use the event's title as the default.  Only letters, numbers, and hyphens can be used in the slug.  Cannot use special charaters or spaces (ex: can't use & or $).  If left blank to use the event's title as the slug, it will remove special characters from the slug for you along with replacing the spaces with hyphens.", max_length=255)
    meta_tags = models.CharField(null=True, blank=True, max_length=510, help_text="Enter keywords separated by commas.  EX: word1, word2, word3  ***IMPORTANT: must separate by commas for it to help SEO***.")
    main_page = models.CharField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        existing_instance = Seo.objects.filter(event=self.event)
        if existing_instance.exists():
            self.id = existing_instance.first().id
        super(Seo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

