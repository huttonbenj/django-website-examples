# Generated by Django 2.0.2 on 2019-11-19 04:04

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_header_title', models.CharField(default='Artwork', help_text='Title for the page with "All Artwork"', max_length=50, verbose_name='Header Title')),
                ('artwork_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "All Artwork"', null=True, verbose_name='Header Image')),
                ('artwork_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('artwork_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('originals_header_title', models.CharField(default='Originals', help_text='Title for the page with "Originals Artwork"', max_length=50, verbose_name='Header Title')),
                ('originals_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "Originals Artwork"', null=True, verbose_name='Header Image')),
                ('originals_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('originals_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('oils_header_title', models.CharField(default='Oils', help_text='Title for the page with "Oils Artwork"', max_length=50, verbose_name='Header Title')),
                ('oils_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "Oils Artwork"', null=True, verbose_name='Header Image')),
                ('oils_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('oils_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('watercolor_header_title', models.CharField(default='Watercolor', help_text='Title for the page with "Watercolor Artwork"', max_length=50, verbose_name='Header Title')),
                ('watercolor_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "Watercolor Artwork"', null=True, verbose_name='Header Image')),
                ('watercolor_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('watercolor_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('prints_header_title', models.CharField(default='Prints', help_text='Title for the page with "Prints Artwork"', max_length=50, verbose_name='Header Title')),
                ('prints_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "Prints Artwork"', null=True, verbose_name='Header Image')),
                ('prints_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('prints_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('framed_header_title', models.CharField(default='Framed', help_text='Title for the page with "Framed Artwork"', max_length=50, verbose_name='Header Title')),
                ('framed_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "Framed Artwork"', null=True, verbose_name='Header Image')),
                ('framed_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('framed_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('unframed_header_title', models.CharField(default='Unframed', help_text='Title for the page with "Unframed Artwork"', max_length=50, verbose_name='Header Title')),
                ('unframed_header_image', pyuploadcare.dj.models.ImageField(help_text='Image for the page with "Unframed Artwork"', null=True, verbose_name='Header Image')),
                ('unframed_gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('unframed_gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('gallery_header', models.CharField(default='Gallery', help_text='Title for the Gallery section on the homepage', max_length=50, verbose_name='Gallery Header')),
                ('gallery_title', models.CharField(default='Gallery', help_text='Title for the gallery on the home page.', max_length=50, verbose_name='Home Page Gallery Title')),
                ('gallery_style', models.CharField(choices=[('staggered', 'staggered'), ('even', 'even')], default='staggered', help_text='If you use the "staggered" style here, you must use pictures in multiples of 12 so it won\'t become uneven.\n        If you don\'t have multiples of 12, use the "even" style.', max_length=50, verbose_name='Gallery Style')),
                ('gallery_columns', models.CharField(choices=[('two_columns', 'two_columns'), ('four_columns', 'four_columns')], default='two_columns', help_text='Number of columns to use for gallery layout.', max_length=50, verbose_name='Gallery Columns')),
                ('image', pyuploadcare.dj.models.ImageField(help_text='This image will appear on all necessary pages which is determined by the category.  Only the most recent 12 uploads will show up on the home page gallery.', null=True)),
                ('image_title', models.CharField(help_text='Image title that appears on mouse hover', max_length=100, null=True, verbose_name='Image Title')),
                ('image_description', models.TextField(help_text='This is the description for your piece of art.', null=True)),
                ('image_category', models.CharField(choices=[('originals', 'originals'), ('prints', 'prints')], help_text='This category determines what pages the image will appear on.  This also determines what categories appear for filtering the galleries.', max_length=100, null=True, verbose_name='Image Category')),
                ('image_sub_category', models.CharField(blank=True, choices=[('oils', 'oils'), ('watercolor', 'watercolor')], help_text='Use this to specify what type of original the image is.', max_length=50, null=True, verbose_name='Sub Category')),
                ('framed_unframed', models.CharField(choices=[('framed', 'framed'), ('unframed', 'unframed')], default='unframed', help_text='Use this to clarify whether the image is framed or unframed.', max_length=50, verbose_name='Framed/Unframed')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price for this piece of art.', max_digits=6, null=True)),
                ('number_of_photos', models.CharField(choices=[('4', '4'), ('8', '8'), ('12', '12')], help_text='Number of photos to display on the homepage gallery.', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Artwork',
            },
        ),
    ]