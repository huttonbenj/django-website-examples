from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .models import CustomUser as User
from .forms import MyProfileSettingsForm

from .forms import NewUserForm
from .models import MyProfile

import json
# Create your views here.

def register(request):
    form = NewUserForm

    # POST
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if len(form.errors) > 0:
            context = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
            }
            return render(request=request,
                        template_name="accounts/register.html",
                        context={"form": form, 'context': context})

        elif form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            create_profile = MyProfile(customuser=request.user)
            create_profile.save()
            user = User(username=username, first_name=first_name, last_name=last_name, email=email, profile=create_profile)
            user.save()

            login(request, user)
            current_user_profile = MyProfile.objects.filter(customuser=request.user).exists()
            if current_user_profile == False:
                create_profile = MyProfile(customuser=request.user)
                create_profile.save()
            return redirect('/')

    else:
        return render(request=request,
                    template_name="accounts/register.html",
                    context={"form": form})

def login_request(request, *args, **kwargs):

    if request.method == 'POST':
    
        form = AuthenticationForm(request=request, data=request.POST)
        next = request.POST.get('next')
        if request.META['HTTP_REFERER'] == '/reservations/create':
            next = '/reservations/create'

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not next == str(None):  
                if user is not None:
                    login(request, user)
                    if next == '/reservations/create':
                        data = {'msg':f"You are now logged in as {username}"}
                        return JsonResponse(data)
                    else:
                        msg = messages.info(request, f"You are now logged in as {username}")
                    return redirect(next)
                else:
                    messages.error(request, "Invalid username or password.")        
            else:
                if user is not None:
                    login(request, user)
                    if next == '/reservations/create':
                        data = {'msg':f"You are now logged in as {username}"}
                        return JsonResponse(data)
                    else:
                        msg = messages.info(request, f"You are now logged in as {username}")
                    return redirect('/')
                else:
                    messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.") 
    else:
        next = request.GET.get('next')

    form = AuthenticationForm()
    
    return render(request=request,
                  template_name="accounts/login.html",
                  context={"form": form, 'next': next})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def reset_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


@login_required(login_url='/login/')
def myprofile(request):
    current_user = request.user

    profile_settings_form = MyProfileSettingsForm
    avatar = current_user.profile.image.cdn_url

    # POST
    if request.method == 'POST':
        profile_settings_form = MyProfileSettingsForm(request.POST)     
        print(profile_settings_form)
        if profile_settings_form.is_valid():
            print('VALID')

            user_profile = User.objects.get(profile=current_user.profile)
            user_profile.image = profile_settings_form.cleaned_data['image']
            user_profile.facebook = profile_settings_form.cleaned_data['facebook']
            user_profile.twitter = profile_settings_form.cleaned_data['twitter']
            user_profile.linkdin = profile_settings_form.cleaned_data['linkdin']
            user_profile.instagram = profile_settings_form.cleaned_data['instagram']
            user_profile.description = profile_settings_form.cleaned_data['description']
            user_profile.save()

            current_user.first_name = profile_settings_form.cleaned_data['first_name']
            current_user.last_name = profile_settings_form.cleaned_data['last_name']
            current_user.email = profile_settings_form.cleaned_data['email']
            current_user.phone = profile_settings_form.cleaned_data['phone']

            current_user.save()

    return render(request, 'accounts/profile.html', {
        'current_user': current_user,
        'user_profile': current_user.profile,
        'avatar': avatar,
        'profile_settings_form': profile_settings_form,
    })
