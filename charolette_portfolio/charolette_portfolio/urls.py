"""charolette_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home.views, header.views, shop.views, artwork.views, cart.views, users.views, events.views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", users.views.register, name="register"),
    path("login/", users.views.login_request, name="login"),
    path("logout/", users.views.logout_request, name="logout"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='main/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='main/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='main/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='main/password_reset_complete.html'
         ),
         name='password_reset_complete'),


    path('', home.views.home, name='home'),
    path('artwork/', artwork.views.artwork, name='artwork'),
    path('originals/', artwork.views.originals, name='originals'),
    path('oil/', artwork.views.oil, name='oil'),
    path('watercolor/', artwork.views.watercolor, name='watercolor'),
    path('prints/', artwork.views.prints, name='prints'),
    path('framed/', artwork.views.framed, name='framed'),
    path('unframed/', artwork.views.unframed, name='unframed'),
    path('cart/', cart.views.cart, name='cart'),
    path('checkout/', cart.views.checkout, name='checkout'),
    path('events/', events.views.events, name='events'),
    path('single_event/', events.views.single_event, name='single_event'),
    path('success/', home.views.successView, name='success')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
