from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect

from .forms import NewUserForm
# Create your views here.

def register(request):

    previous_url = request.GET.get('previous_url')
    keep_shopping = request.GET.get('keep_shopping')
    checkout = request.GET.get('checkout')
    item = request.GET.get('item')
    cart_link = request.GET.get('cart_link')
    login_link = request.GET.get('login_link')
    referrer = request.GET.get('referrer')
    reset = request.GET.get('reset')

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)

            previous_url = request.POST.get('previous_url')
            keep_shopping = request.POST.get('keep_shopping')
            checkout = request.POST.get('checkout')
            item = request.POST.get('item')
            cart_link = request.POST.get('cart_link')
            login_link = request.POST.get('login_link')
            referrer = request.POST.get('referrer')
            reset = request.POST.get('reset')

            if str(reset) == 'True': return redirect('home')
            if str(previous_url) == "gallery": return redirect(referrer)
            if str(login_link) == "True": return redirect(f'{previous_url}')
            if str(keep_shopping) == "True": return redirect(f'/cart/?item={item}&keep_shopping=True&previous_url={previous_url}')
            if str(checkout) == "True": return redirect(f'/cart/?item={item}&checkout=True')
            if str(previous_url) == "cart" and str(cart_link) == "True": return redirect(f'/cart/?cart_link=True')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = NewUserForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form, 'previous_url': previous_url, 'keep_shopping': keep_shopping, 'checkout': checkout, 'item': item, 'cart_link': cart_link, 'login_link': login_link, 'referrer': referrer, 'reset':reset})

def login_request(request, *args, **kwargs):
    
    #### GET PREVIOUS URL ####
    referrer = request.META.get('HTTP_REFERER')
    referrer = referrer.split('/')
    referrer = [s for s in referrer if s == 'artwork' or s == 'originals' or s == 'oil' or s == 'watercolor' or s == 'prints' or s == 'framed' or s == 'unframed' or s == 'login']
    referrer = 'home' if referrer == [] else referrer[0]


    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                msg = messages.info(request, f"You are now logged in as {username}")
                previous_url = request.POST.get('previous_url')
                keep_shopping = request.POST.get('keep_shopping')
                checkout = request.POST.get('checkout')
                item = request.POST.get('item')
                cart_link = request.POST.get('cart_link')
                login_link = request.POST.get('login_link')
                referrer = request.POST.get('referrer')
                reset = request.POST.get('reset')

                if str(reset) == 'True': return redirect('home')
                if str(previous_url) == "gallery": return redirect(referrer)
                if str(login_link) == "True": return redirect(f'{previous_url}')
                if str(keep_shopping) == "True": return redirect(f'/cart/?item={item}&keep_shopping=True&previous_url={previous_url}')
                if str(checkout) == "True": return redirect(f'/cart/?item={item}&checkout=True')
                if str(previous_url) == "cart" and str(cart_link) == "True": return redirect(f'/cart/?cart_link=True')

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    previous_url = request.GET.get('previous_url')
    keep_shopping = request.GET.get('keep_shopping')
    checkout = request.GET.get('checkout')
    item = request.GET.get('item')
    cart_link = request.GET.get('cart_link')
    login_link = request.GET.get('login_link')
    reset = request.GET.get('reset')


    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form, 'previous_url': previous_url, 'keep_shopping': keep_shopping, 'checkout': checkout, 'item': item, 'cart_link':cart_link, 'login_link':login_link, 'referrer':referrer, 'reset':reset})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def reset_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'main/change_password.html', args)
