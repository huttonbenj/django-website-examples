from django.contrib import admin
from .models import MyProfile, CustomUser
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, SetPasswordForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

# Register your models here.
@admin.register(MyProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name',]


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'phone')


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    
    error_messages = {
        **SetPasswordForm.error_messages,
        'password_incorrect': ("Your old password was entered incorrectly. Please enter it again."),
    }
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    field_order = ['old_password', 'new_password1', 'new_password2']


    def clean_password2(self):
        # Check that the two password entries match
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Passwords don't match")
        return new_password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserChangeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["new_password2"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('username', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields':  ('username', 'first_name', 'last_name', 'email', 'old_password', 'new_password1', 'new_password2', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)


    def save_model(self, request, obj, form, change):
        super(CustomUserAdmin, self).save_model(
                request, obj, form, change)
        if change == False:    
            create_profile = MyProfile(customuser=obj)
            create_profile.name = obj.first_name + obj.last_name
            create_profile.save()
        
        exists = MyProfile.objects.filter(customuser=obj).exists()
        if change == True and exists == False:
            create_profile = MyProfile(customuser=obj)
            create_profile.name = obj.first_name + ' ' + obj.last_name
            create_profile.save()

        
# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)