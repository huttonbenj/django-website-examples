
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home_portfolio.views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home_portfolio.views.home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
