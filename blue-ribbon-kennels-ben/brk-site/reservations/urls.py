from django.urls import path, include
from .views import calc_cost, get_obj_id, get_unavailable_dates, create, successful_registration, get_monthly_sum_info

urlpatterns = [
    # path('configuration/', create),
    path('create/', create, name='create'),
    path('ajax/calc_cost/', calc_cost),
    path('ajax/get_unavailable_dates/', get_unavailable_dates),
    path('ajax/get_obj_id/', get_obj_id),
    path('ajax/get_monthly_sum_info/', get_monthly_sum_info),
    path('successful_registration/', successful_registration, name='successful_registration'),

]
