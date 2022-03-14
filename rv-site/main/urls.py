"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from contact import views as contact_views 

admin.site.app_index_template = 'admin/custom_app_list.html'

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),

    path('', include('home.urls')),
    path('lots/', include('lots.urls')),
    path('rates/', include('rates.urls')),
    path('reserve/', include('reserve.urls')),
    path('blog/', include('blog.urls')),
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('ownership/', include('ownership.urls')),
    path('specials/', include('specials.urls')),
    path('contact/', include('contact.urls')),
    path('beach_access/', include('beach_access.urls')),
    path('GARV/', include('garv.urls')),
    path('garv/', include('garv.urls')),
    
    path('caldera_forms_preview/', contact_views.email_form_submit, name='caldera_forms_preview'),
    path('rv-specifications/', contact_views.email_form_submit, name='rv-specifications'),

    path('', include('djangocms_forms.urls'), name='forms'),
    path('', include('cms.urls')),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
