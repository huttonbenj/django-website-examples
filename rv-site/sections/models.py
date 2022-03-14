
from django.db import models
from pyuploadcare.dj.models import ImageField, FileField

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Header(models.Model):
    logo_white = models.ImageField(null=True, blank=False, help_text="250x250 is the preferred size.  This logo is displayed in the navbar BEFORE a visitor begins to scroll down.")
    logo_colors = models.ImageField(null=True, blank=False, help_text="250x250 is the preferred size.  This logo is displayed in the navbar AFTER a visitor begins to scroll down.")

    def save(self, *args, **kwargs):
        self.id = 1
        super(Header, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'header'
        verbose_name_plural = 'header'

class Slider(models.Model):
    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'slider'
        
class Slide(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE)
    background_image = models.ImageField(null=True, blank=True, help_text="This image is the first thing you see when visiting Buena Vista. It is displayed on the home page and covers the full size of the screen.  Large images are preferred here otherwise it will become distorted.")
    title_small = models.CharField(null=True, blank=False, max_length=255, verbose_name='Meta Title', help_text="This text is smaller font than the main title and is meant to supplement it. It is located directly above the main title.")
    title_large = models.CharField(null=True, blank=False, max_length=255, verbose_name="Main Title", help_text="This text has large font and is meant to be the focal point of the slide (the main title).  It is located just below the Meta Title.")
    description = RichTextUploadingField(null=True, blank=False, verbose_name="Span One", help_text="This text has a smaller font and is meant to be descriptive text.  It is located just below the main title and just above Span Two.")
    description_span = models.CharField(null=True, blank=False, max_length=25, verbose_name="Span Two", help_text="This text is located below Span One and just above the Book Now and Ownership buttons.  Like Span One, it is meant to be descriptive text and has a smaller font.")
    button_1_label = models.CharField(null=True, blank=False, max_length=25, verbose_name="Button One", help_text="When clicked, this button will redirect the visitor to the Reserve page.")
    button_2_label = models.CharField(null=True, blank=False, max_length=25, verbose_name="Button Two", help_text="When clicked, this button will redirect the visitor to the Ownership page (which shows lots for sale).")
    order_slot = models.IntegerField(null=True, blank=False, help_text="Arrange the order the slides show in (lowest to highest).")

class Intro(models.Model):
    image_one = models.ImageField(null=True, blank=True, verbose_name="Animated Image One", help_text="This is smaller than Animated Image Two and it overlays Animated Image Two.  This image will animate in as the visitor is scrolling down.")
    image_two = models.ImageField(null=True, blank=True, verbose_name="Animated Image Two", help_text="This is larger than Animated Image One and it is placed behind Animated Image One.  This image will animate in as the visitor is scrolling down. ")
    title = models.CharField(null=True, blank=False, max_length=255, help_text="The title for this section is located on the top-left half of the section beside the two animated images.")
    description = RichTextUploadingField(null=True, blank=False, help_text="The description for this section is located on the bottom-left half of the section just under the title and beside the animated images.")

    def save(self, *args, **kwargs):
        self.id = 1
        super(Intro, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'intro'
        verbose_name_plural = 'intro'

class Overview(models.Model):
    icon = models.FileField(null=True, blank=False, help_text="Upload an .svg file.  This is located just above the title of this column of the section (there are three columns in this section).")
    title_small = models.CharField(null=True, blank=False, max_length=255, verbose_name="Meta Title", help_text="This is located just above the main title of this column and has smaller text than the Main Title (meant to be descriptive")
    title_large = models.CharField(null=True, blank=False, max_length=255, verbose_name="Main Title", help_text="This is the main title of the column and has larger text than the Meta Title (meant to be the focal point of the column).")
    description = RichTextUploadingField(null=True, blank=False, help_text="This is located just below the Main Title of the column.")
    position_slot = models.IntegerField(null=True, blank=False, unique=True, help_text="There are 3 columns so use 1, 2, or 3 (this arranges the columns in the order you'd like for this section).")

    class Meta:
        verbose_name = 'overview'
        verbose_name_plural = 'overview'

class Packages(models.Model):
    name = models.CharField(null=True, choices=(('1', 'Standard'), ('2', 'Moderate'), ('3', 'Deluxe'), ('4', 'Luxury')), blank=False, max_length=25, help_text="Select a package.")

    class Meta:
        verbose_name = 'packages'
        verbose_name_plural = 'packages'

class PackageItem(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    background_image = models.ImageField(null=True, blank=True, help_text="Image for this column of the packages section on the home page (there are 4 columns in this section, one for each package).")
    short_description = models.CharField(null=True, blank=False, max_length=255, verbose_name="Meta Description", help_text="This is a shorter description that is shown on this package's column of the section BEFORE a user hovers over this column.")
    long_description = RichTextUploadingField(null=True, blank=False, verbose_name="Main Description", help_text="This is a longer description that animates in when a user hovers over this package's column of the section.")
    button_label = models.CharField(null=True, blank=False, max_length=25, verbose_name="Button", help_text="When clicked, this button redirects to the Reserve page.  This button is located at the bottom of the column under the descriptions.")

    class Meta:
        verbose_name = 'detail'
        verbose_name_plural = 'details'

class About(models.Model):
    icon = models.FileField(null=True, blank=False, help_text="Upload an .svg (icon) to be displayed for this detail in the about section.  This is located just left of the detail's title.")
    title = models.CharField(null=True, blank=False, max_length=25, help_text="Title for this detail of the about section.  Located to the right of this detail's icon and above the description.")
    description = RichTextUploadingField(null=True, blank=False, help_text="Description for this detail of the about section.  Located under the detail's title.")
    position_slot = models.IntegerField(null=True, blank=False, unique=True, help_text="Details will be arranged from lowest to highest so use this number to choose where you want this detail placed in the about section.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about feature'
        verbose_name_plural = 'about features'

class Testimonials(models.Model):
    background_image = models.ImageField(null=True, blank=True, help_text="The image displayed as a background across the whole testimonial section of the homepage.  Large images are required, otherwise it may not scale properly.")

    def __str__(self):
        return f'Testimonials Section'

    class Meta:
        verbose_name = 'testimonials'
        verbose_name_plural = 'testimonial'

class Testimonial(models.Model):
    testimonial = models.ForeignKey(Testimonials, on_delete=models.CASCADE, related_name='testimonial')
    avatar = models.ImageField(null=True, blank=True, help_text="This is profile type image of the visitor who gave the testimonial.")
    first_name = models.CharField(null=True, blank=False, max_length=255, help_text="First name of visitor who gave the testimonial.")
    last_name = models.CharField(null=True, blank=False, max_length=255, help_text="Last name of the visitor who gave the testimonial.")
    story = RichTextUploadingField(null=True, blank=False, help_text="This is the actual testimonial given by the visitor.")
    location = models.CharField(null=True, blank=False, max_length=255, help_text="This is where the visitor is from.")

    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonial'

class Footer(models.Model):
    logo = models.ImageField(null=True, blank=False, help_text="250x250 is the preferred size.  This logo is displayed in the top left of the footer.")

    def save(self, *args, **kwargs):
        self.id = 1
        super(Footer, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'footer'
        verbose_name_plural = 'footer'

       
