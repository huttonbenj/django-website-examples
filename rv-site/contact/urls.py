from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form_submit, name='contact_form_submit'),
    path('footer/', views.contact_form_submit_footer, name='contact_form_submit_footer'),
    path('lot/', views.contact_form_submit_lots, name='contact_form_submit_lot'),   
]
