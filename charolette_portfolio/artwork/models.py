from django.db import models
from pyuploadcare.dj.models import ImageField


IMAGE_CATERGORY_CHOICES = (
    ('originals', 'originals'),
    ('prints', 'prints'),
)

SUBCATERGORY_CHOICES = (
    ('oils', 'oils'),
    ('watercolor', 'watercolor'),
)

FRAMED_UNFRAMED_CHOICES = (
    ('framed', 'framed'),
    ('unframed', 'unframed'),
)

# Create your models here.
class Artwork(models.Model):

    # All Artwork
    artwork_header_title = models.CharField(default='Artwork', max_length=50, verbose_name='Header Title', help_text='Title for the page with "All Artwork"')
    artwork_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "All Artwork"')
    artwork_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    artwork_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # Originals
    originals_header_title = models.CharField(default='Originals', max_length=50, verbose_name='Header Title', help_text='Title for the page with "Originals Artwork"')
    originals_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "Originals Artwork"')
    originals_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    originals_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')
    
    # Oils
    oils_header_title = models.CharField(default='Oils', max_length=50, verbose_name='Header Title', help_text='Title for the page with "Oils Artwork"')
    oils_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "Oils Artwork"')
    oils_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    oils_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # Watercolor
    watercolor_header_title = models.CharField(default='Watercolor', max_length=50, verbose_name='Header Title', help_text='Title for the page with "Watercolor Artwork"')
    watercolor_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "Watercolor Artwork"')
    watercolor_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    watercolor_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # Prints
    prints_header_title = models.CharField(default='Prints', max_length=50, verbose_name='Header Title', help_text='Title for the page with "Prints Artwork"')
    prints_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "Prints Artwork"')
    prints_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    prints_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # Framed
    framed_header_title = models.CharField(default='Framed', max_length=50, verbose_name='Header Title', help_text='Title for the page with "Framed Artwork"')
    framed_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "Framed Artwork"')
    framed_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    framed_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # Unframed
    unframed_header_title = models.CharField(default='Unframed', max_length=50, verbose_name='Header Title', help_text='Title for the page with "Unframed Artwork"')
    unframed_header_image = ImageField(null=True, verbose_name='Header Image', help_text='Image for the page with "Unframed Artwork"')
    unframed_gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    unframed_gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # Home Page Gallery
    gallery_header = models.CharField(default='Gallery', max_length=50, verbose_name='Gallery Header', help_text='Title for the Gallery section on the homepage')
    gallery_title = models.CharField(default='Gallery', max_length=50, verbose_name='Home Page Gallery Title', help_text='Title for the gallery on the home page.')
    gallery_style = models.CharField(default='staggered', choices=(
        ('staggered', 'staggered'), ('even', 'even')), max_length=50,
        help_text='''If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.
        If you don\'t have multiples of 12, use the "even" style.''', verbose_name='Gallery Style')
    gallery_columns = models.CharField(default='two_columns', choices=(
        ('two_columns', 'two_columns'), ('four_columns', 'four_columns')), max_length=50,
        help_text='''Number of columns to use for gallery layout.''', verbose_name='Gallery Columns')

    # This applies to all galleries
    image = ImageField(null=True, help_text='This image will appear on all necessary pages which is determined by the category.  Only the most recent 12 uploads will show up on the home page gallery.')
    image_title = models.CharField(null=True, max_length=100, verbose_name='Image Title', help_text="Image title that appears on mouse hover")
    image_description = models.TextField(null=True, help_text='This is the description for your piece of art.')
    image_category = models.CharField(null=True, choices=IMAGE_CATERGORY_CHOICES, max_length=100, verbose_name='Image Category', help_text="This category determines what pages the image will appear on.  This also determines what categories appear for filtering the galleries.")
    image_sub_category = models.CharField(null=True, blank=True, choices=SUBCATERGORY_CHOICES, max_length=50, verbose_name='Sub Category', help_text='Use this to specify what type of original the image is.')
    framed_unframed = models.CharField(choices=FRAMED_UNFRAMED_CHOICES, default='unframed', max_length=50, verbose_name='Framed/Unframed', help_text='Use this to clarify whether the image is framed or unframed.')
    price = models.DecimalField(null=True, help_text='Price for this piece of art.', max_digits=6, decimal_places=2)


    number_of_photos = models.CharField(choices=(('4', '4'), ('8', '8'), ('12', '12')), max_length=20, help_text='Number of photos to display on the homepage gallery.')
    

    class Meta:
        verbose_name_plural = 'Artwork'

    def __str__(self):
        return 'Artwork: ' + self.image_title
