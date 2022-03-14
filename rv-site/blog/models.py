from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=False, max_length=255, unique=True, help_text='Will appear as title on both the blog feed along with the individual blog post page.')
    image = models.ImageField(null=True, blank=True, help_text='Will be shown on the blog feed as a preview image and on the individual blog post page.')
    story = RichTextUploadingField(null=True, blank=False, help_text='The actual content for the blog.')
    datetime = models.DateTimeField(null=True, verbose_name='date to publish', help_text='Determines the day and time to post the blog live on the website.')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Post'


class Categories(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    category = models.CharField(null=True, blank=False, max_length=50, help_text='Categories are shown beside the blog title on both the blog feed and individual blog page.')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class PageTitle(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=255, help_text="FOR BLOG POSTS: leave blank to use the blog's title as the default.  FOR BLOG FEED: must enter value.  This is shown at the top of the page.")
    description = models.TextField(null=True, blank=True, help_text='The description is directly under the page title at the top of the page.')
    background_image = models.ImageField(null=True, blank=True, help_text="FOR BLOG POSTS: leave blank to use the blog's image as the default.  FOR BLOG FEED: must enter value.  This is shown at the top of the page directly behind the page title and description.")

    class Meta:
        verbose_name = 'Page Title/SEO'
        verbose_name_plural = 'Page Title/SEO'

class Seo(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    page_title = models.ForeignKey(PageTitle, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=255, help_text="FOR BLOG POSTS: leave blank to use the blog's title as the default.  FOR BLOG FEED: must enter a value.  This is used for SEO purposes and is not visible to users anywhere on the website.")
    description = models.TextField(null=True, blank=True, help_text="FOR BLOG POSTS: leave blank to use the blog's story as the default.  FOR BLOG FEED: must enter a value.  This is used for SEO purposes and is not visible to users anywhere on the website.")
    slug = models.SlugField(null=True, blank=True, unique=True, help_text="Leave blank to use the blog's title as the default.  Only letters, numbers, and hyphens can be used in the slug.  Cannot use special charaters or spaces (ex: can't use & or $).  If left blank to use the blog's title as the slug, it will remove special characters from the slug for you along with replacing the spaces with hyphens.", max_length=255)
    meta_tags = models.CharField(null=True, blank=True, max_length=510, help_text="Enter keywords separated by commas.  EX: word1, word2, word3  ***IMPORTANT: must separate by commas for it to help SEO***.")
    main_page = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

