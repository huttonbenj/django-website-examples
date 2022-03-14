from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.functional import empty
from stripe.api_resources import payment_method, setup_intent
from stripe.api_resources.checkout import session
from .models import *
from django.views.generic import ListView, CreateView, DetailView, TemplateView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from main.models import Logo
from reservations.models import Reservation, Kennel
from accounts.models import CustomUser, MyProfile

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

@csrf_exempt
def create_checkout_session(request, id):

    request_data = json.loads(request.body)
    product = get_object_or_404(Product, id=id.split('-')[0])

    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    for entry in request_data['form_data']:
        print(entry['name'])
        request_data[entry['name']] = entry['value']

    customer = stripe.Customer.create(
        description="My First Test Customer (created for API docs)",
        email=request_data['email']
    )

    payment_method = stripe.PaymentMethod.create(
        type="card",
        card={
            "number": request_data['booking-registration-card-no'],
            "exp_month": int(request_data['booking-registration-card-exp'].split('/')[0]),
            "exp_year": int(request_data['booking-registration-card-exp'].split('/')[1]),
            "cvc": request_data['booking-registration-card-cvv'],
        },
        billing_details={
            "address": {
                "city": request_data['city'],
                "country": 'US',
                "line1": request_data['street'],
                "line2": None,
                "postal_code": request_data['postal_code'],
                "state": request_data['state']
            },
            'email':request_data['email'],
            'name':request_data['first_name']+ ' '+request_data['last_name'],
            'phone':request_data['phone']
        },
    )

    payment_method = stripe.PaymentMethod.attach(
        payment_method.id,
        customer=customer.id,
    )

    customer['payment_method'] = payment_method.id

    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        # customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(request_data['paid_amount'])*100,
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
        customer=customer.id,
    )

    start_date_additional = None
    end_date_additional = None
    additional_cost = None
    pickup_date = datetime.datetime.strptime(request_data['id_end_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
    if 'id_end_date_additional' in request_data.keys():
        pickup_date = datetime.datetime.strptime(request_data['id_end_date_additional'], '%m/%d/%Y').strftime('%Y-%m-%d')
        start_date_additional = datetime.datetime.strptime(request_data['id_start_date_additional'], '%m/%d/%Y').strftime('%Y-%m-%d')
        end_date_additional = pickup_date
        additional_cost = request_data['additional-cost']
    
    existing_reservation = Reservation.objects.filter(id=id.split('-')[1])
    print(existing_reservation.last().id)
    if not existing_reservation.exists():
        reservation = Reservation.objects.create(
            kennel=Kennel.get_availabile(),
            payment=product,
            type=get_restype(request_data),
            start_date=datetime.datetime.strptime(request_data['id_start_date'], '%m/%d/%Y').strftime('%Y-%m-%d'),
            end_date=datetime.datetime.strptime(request_data['id_end_date'], '%m/%d/%Y').strftime('%Y-%m-%d'), 
            start_date_additional=start_date_additional,
            end_date_additional=end_date_additional, 
            extended_stay=request_data['extended-stay'],
            pickup_date=pickup_date,
            number_of_days=request_data['day-diff'],
            cost=request_data['initial-cost'],
            additional_cost=additional_cost,
            overall_cost=request_data['total-cost'],
            first_name=request_data['first_name'], 
            last_name=request_data['last_name'], 
            email=request_data['email'],
            phone=request_data['phone'],
            street=request_data['street'],
            city=request_data['city'],
            state=request_data['state'],
            postal_code=request_data['postal_code'],
            dogs_name=request_data['dogs_name'], 
            dogs_breed=request_data['dogs_breed'],
            dogs_sex=request_data['dogs_sex'],
            dogs_age=int(request_data['dogs_age']),
            comments=request_data['comments'],
            session_key=request.session.session_key,
        )
    elif existing_reservation.exists():
        reservation = existing_reservation.last()
        reservation.type = get_restype(request_data),
        reservation.start_date = datetime.datetime.strptime(request_data['id_start_date'], '%m/%d/%Y').strftime('%Y-%m-%d'),
        reservation.end_date = datetime.datetime.strptime(request_data['id_end_date'], '%m/%d/%Y').strftime('%Y-%m-%d'), 
        reservation.start_date_additional = start_date_additional,
        reservation.end_date_additional=end_date_additional, 
        reservation.extended_stay=request_data['extended-stay'],
        reservation.pickup_date=pickup_date,
        reservation.number_of_days=request_data['day-diff'],
        reservation.cost=request_data['initial-cost'],
        reservation.additional_cost=additional_cost,
        reservation.overall_cost=request_data['total-cost'],
        reservation.first_name=request_data['first_name'], 
        reservation.last_name=request_data['last_name'], 
        reservation.email=request_data['email'],
        reservation.phone = request_data['phone'],
        reservation.street=request_data['street'],
        reservation.city=request_data['city'],
        reservation.state=request_data['state'],
        reservation.postal_code=request_data['postal_code'],
        reservation.dogs_name=request_data['dogs_name'], 
        reservation.dogs_breed=request_data['dogs_breed'],
        reservation.dogs_sex=request_data['dogs_sex'],
        reservation.dogs_age=int(request_data['dogs_age']),
        reservation.comments=request_data['comments'],        
    reservation.save()

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    payment = product
    payment.customer_email = request_data['email']
    payment.customer_name = f'{reservation.first_name} {reservation.last_name}' 
    payment.stripe_payment_intent = checkout_session['payment_intent']
    payment.amount = int(request_data['day-diff'])
    payment.total_cost = int(reservation.overall_cost)
    payment.amount_paid = int(request_data['paid_amount'])
    payment.amount_owed = payment.total_cost - int(request_data['paid_amount'])
    if payment.amount_paid < payment.total_cost:
        payment.paid_in_full = False
    elif payment.amount_paid == payment.total_cost:
        payment.paid_in_full = True
    payment.save()

    # return JsonResponse({'data': checkout_session})

    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = "payments/payment_success.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentSuccessView, self).get_context_data(**kwargs)
        context['logo'] = Logo.objects.last()
        return context  

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(
            Product, stripe_payment_intent=session.payment_intent)
        order.has_paid = True
        order.save()
        
        return render(request, self.template_name, context=self.get_context_data())


class PaymentFailedView(TemplateView):
    template_name = "payments/payment_failed.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentFailedView, self).get_context_data(**kwargs)
        context['logo'] = Logo.objects.last()
        return context  
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())