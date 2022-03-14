
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.core.mail import send_mail
from phone_field import PhoneField

from .managers import CustomUserManager


class MyProfile(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    image = models.ImageField(default='https://ucarecdn.com/32641ede-91e2-4eaf-ad4a-043facc9220a/avatar.jpg')
    # banner_image = models.ImageField(default='https://ucarecdn.com/869ee452-bf08-47ca-9845-d4d5244ad78a/blueandwhitebackgroundbluewhitebackground1600x1200.jpg')

    # facebook = models.URLField(blank=True, default='', max_length=300)
    # twitter = models.URLField(blank=True, default='', max_length=300)
    # linkdin = models.URLField(blank=True, default='', max_length=300)
    # instagram = models.URLField(blank=True, default='', max_length=300)

    description = models.CharField(null=True, blank=True, max_length=300)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True, null=True, max_length=254)
    phone = PhoneField(_('phone'), blank=True, null=True)
    street = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    state = models.CharField(null=True, blank=True, max_length=255)
    postal_code = models.IntegerField(null=True, blank=True)


    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    profile = models.ForeignKey(MyProfile, on_delete=models.CASCADE, null=True)


    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"








