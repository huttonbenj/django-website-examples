from django.forms.forms import Form
from django.shortcuts import render

from django.http import JsonResponse
from .models import Reservation, Kennel
from main.models import Logo
from .forms import ReservationForm
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.conf import settings
from payments.models import Product 
from accounts.models import CustomUser
from datetime import timedelta, datetime
from collections import OrderedDict
import json
from django.contrib.auth.forms import AuthenticationForm
from django.middleware.csrf import get_token

def get_restype(data):
    keys = data.keys()
    if 'boarding' in keys:
        res_type = 'boarding'
    if 'boarding_and_training' in keys:
        res_type = 'boarding_and_training'
    elif 'obedience_training' in keys:
        res_type = 'obedience_training'
    elif 'retriever_training' in keys:
        res_type = 'retriever_training'
    return res_type


def calc_cost(request):
    reservation_type = request.GET.get('type', None)
    num_days = request.GET.get('numDays', None)
    pricing_details = Reservation.get_pricing(reservation_type)

    if not pricing_details['minimum']:
        total_cost = pricing_details['price']*int(num_days)

    else:
        total_cost = pricing_details['price']*pricing_details['minimum']
            
    data = {
        'total_cost': total_cost
    }

    return JsonResponse(data)

def create(request):
    form = ReservationForm

    if not request.session.session_key:
        request.session.create()
    
    if request.user.is_authenticated:
        usr = CustomUser.objects.get(id=request.user.id)
        form =  ReservationForm(initial={
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'email': usr.email,
            'phone': usr.phone,
            'street': usr.street,
            'city': usr.city,
            'state': usr.state,
            'postal_code': usr.postal_code,
            # 'dogs_breed': usr.dogs_breed,
            # 'dogs_name': usr.dogs_name,
            # 'dogs_age': usr.dogs_age,
            # 'dogs_sex': usr.dogs_sex,
            # 'shot_records': usr.shot_records,
        })

    csrf_token = get_token(request)

    ctx = {
        'logo': Logo.objects.last(),
        'form': form,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'products': Product.objects.all(),
        'auth_form': AuthenticationForm,
        'csrf_token_html': csrf_token

    }
    return render(request, 'reservations/create.html', context=ctx)

def get_unavailable_dates(request):
    reservation_type = request.GET.get('reservationType', None)
    data = {
        'unavailable_dates': Reservation.get_unavailable(reservation_type), 
    }
    return JsonResponse(data)

def get_obj_id(request):
    request_data = dict()
    for entry in request.POST:
        request_data[entry] = request.POST[entry]
    
    obj = Product.objects.create(name=get_restype(request_data), price=request_data['price'], session_key=request.session.session_key)
    obj.save()

    shot_records = None
    if request.FILES:
        shot_records = request.FILES.get('shot_records')
    reservation = Reservation.objects.create(kennel=Kennel.get_availabile(), payment=obj, shot_records=shot_records, session_key=request.session.session_key)
    reservation.save()
    data = {'obj_id': obj.id, 'res_id':reservation.id }

    return JsonResponse(data)

def get_monthly_sum_info(request):
 
    N_DAYS_AGO = 90

    today = datetime.now()    
    n_days_ago = today - timedelta(days=N_DAYS_AGO)
    payments = Product.objects.filter(created_on__gte=n_days_ago, total_cost__isnull=False, amount_paid__isnull=False, amount_owed__isnull=False).order_by('created_on')
    total_expected_revenue = 0
    amount_owed = 0
    amount_paid = 0
    dates = OrderedDict()
    for payment in payments:
        total_expected_revenue+=payment.total_cost
        amount_owed+=payment.amount_owed
        amount_paid+=payment.amount_paid
        if not str(payment.created_on.date()) in dates.keys():
            dates[str(payment.created_on.date())] = {'daily_revenue': payment.total_cost, 'daily_amount_owed':payment.amount_owed, 'daily_amount_paid':payment.amount_paid}
        else:
            daily_revenue = int(dates[str(payment.created_on.date())]['daily_revenue']) + int(payment.total_cost)
            daily_amount_owed = int(dates[str(payment.created_on.date())]['daily_amount_owed']) + int(payment.amount_owed)
            daily_amount_paid = int(dates[str(payment.created_on.date())]['daily_amount_paid']) + int(payment.amount_paid)
            dates[str(payment.created_on.date())] = {'daily_revenue': daily_revenue, 'daily_amount_owed':daily_amount_owed, 'daily_amount_paid':daily_amount_paid}
    daily_rev = list()
    daily_owed = list()
    daily_paid = list()
    date_keys = [str(date) for date in dates.keys()]
    for k,v in dates.items():
        daily_rev.append(v['daily_revenue'])
        daily_owed.append(v['daily_amount_owed'])
        daily_paid.append(v['daily_amount_paid'])

    print(daily_rev)
    data = {
        'total_expected_revenue':total_expected_revenue,
        'amount_paid':amount_paid,
        'amount_owed':amount_owed,
        'dates':dates,
        'date_keys':date_keys,
        'daily_rev':daily_rev,
        'daily_owed':daily_owed,
        'daily_paid':daily_paid
    }
    return JsonResponse(data)


def successful_registration(request):
    ctx = {
        'logo': Logo.objects.last(),
    }

    request_data = request.GET

    start_date_additional = None
    end_date_additional = None
    additional_cost = None
    pickup_date = datetime.strptime(request_data['id_end_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
    if 'id_end_date_additional' in request_data.keys():
        pickup_date = datetime.strptime(request_data['id_end_date_additional'], '%m/%d/%Y').strftime('%Y-%m-%d')
        start_date_additional = datetime.strptime(request_data['id_start_date_additional'], '%m/%d/%Y').strftime('%Y-%m-%d')
        end_date_additional = pickup_date
        additional_cost = request_data['additional-cost']

    if request_data['extended-stay'] == 'false':
        extended_stay = False
    elif request_data['extended-stay'] == 'true':
        extended_stay = True
    
    product = Product.objects.create(name=get_restype(request_data), price=request_data['total-cost'], customer_email=request_data['email'], amount=request_data['day-diff'], has_paid=False, paid_in_full=False)
    product.save()
   
    reservation = Reservation.objects.create(
        kennel=Kennel.get_availabile(),
        payment=product,
        type=get_restype(request_data),
        start_date=datetime.strptime(request_data['id_start_date'], '%m/%d/%Y').strftime('%Y-%m-%d'),
        end_date=datetime.strptime(request_data['id_end_date'], '%m/%d/%Y').strftime('%Y-%m-%d'), 
        start_date_additional=start_date_additional,
        end_date_additional=end_date_additional, 
        extended_stay=extended_stay,
        pickup_date=pickup_date,
        number_of_days=request_data['day-diff'],
        cost=request_data['initial-cost'],
        additional_cost=additional_cost,
        overall_cost=request_data['total-cost'],
        first_name=request_data['first_name'], 
        last_name=request_data['last_name'], 
        email=request_data['email'],
        phone='+1'+request_data['phone'],
        street=request_data['street'],
        city=request_data['city'],
        state=request_data['state'],
        postal_code=request_data['postal_code'],
        dogs_name=request_data['dogs_name'], 
        dogs_breed=request_data['dogs_breed'],
        dogs_sex=request_data['dogs_sex'],
        dogs_age=int(request_data['dogs_age']),
        comments=request_data['comments'],
        session_key = request.session.session_key,
    )
    reservation.save()

    return render(request, 'reservations/successful-registration.html', context=ctx)