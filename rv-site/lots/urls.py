from django.urls import path
from . import views

urlpatterns = [
    path('', views.lot_map, name='lot-map'),
    path('single/<int:id>/', views.single, name='lot_single'),
]
