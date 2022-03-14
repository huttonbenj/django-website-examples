from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(null=True, blank=False, max_length=100)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(null=True, blank=False, max_length=100)
    message = models.TextField(null=True, blank=False)
    
    class Meta:
        verbose_name = 'Form Submission'
        verbose_name_plural = 'Form Submissions'