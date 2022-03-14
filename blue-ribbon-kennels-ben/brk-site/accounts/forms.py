from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser as User
from .models import MyProfile

ACCOUNT_TYPE_CHOICES = (
    ('free', 'free'),
    ('paid', 'paid')
)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


class MyProfileSettingsForm(forms.Form):
    image = forms.ImageField(label='')
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True, max_length=254)
    phone = forms.CharField(required=False)

    facebook = forms.URLField(required=False)
    twitter = forms.URLField(required=False)
    linkdin = forms.URLField(required=False)
    instagram = forms.URLField(required=False)

    description = forms.CharField(max_length=300, required=False)


    class Meta:
        model = MyProfile
        # fields = ('image', 'facebook', 'twitter', 'linkdin', 'instagram')


# class UserProfileRelationForm(forms.Form):
#     first_name = forms.CharField(max_length=50, required=True)
#     last_name = forms.CharField(max_length=50, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(max_length=20, required=False)

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'phone')