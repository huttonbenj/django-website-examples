from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile

@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
