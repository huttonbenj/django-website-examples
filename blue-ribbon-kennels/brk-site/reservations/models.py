from typing import Type
from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
import datetime
import pandas as pd
from phonenumber_field.modelfields import PhoneNumberField
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from payments.models import Product

RESERVATION_TYPES = (
    ('boarding', 'Boarding'),
    ('boarding_and_training', 'Boarding and General Training'),
    ('obedience_training', 'Obedience Training'),
    ('retriever_training', 'Retriever Training'),
)

def current_future_date(value):
    if value < datetime.datetime.today().date():
        raise ValidationError('Only current and future dates are allowed.')

class Kennel(models.Model):
    number = models.IntegerField(null=True, blank=False)
    booked = models.BooleanField(default=False)
    transfer_kennel_to = models.CharField(max_length=25, choices=((str(num), str(num)) for num in range(1,57)), null=True, blank=True)

    @classmethod
    def get_kennel_count(cls):
        return cls.objects.all().count()

    @classmethod
    def get_availabile(cls):
        return cls.objects.filter(booked=False).order_by('number').first()

    def clean(self):
        super().clean()
        if self.transfer_kennel_to:
            if Kennel.objects.get(number=self.transfer_kennel_to).booked:
                raise ValidationError('The kennel you are transfering to is actively booked.')

    def __str__(self):
        return f'Kennel {self.number}'


class Reservation(models.Model):
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    payment = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True, blank=False, choices=RESERVATION_TYPES)
    # start_date = models.DateField(null=True, blank=False, validators=[current_future_date])
    # end_date = models.DateField(null=True, blank=False, validators=[current_future_date])
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    start_date_additional = models.DateField(null=True, blank=True)
    end_date_additional = models.DateField(null=True, blank=True)
    extended_stay = models.BooleanField(default=False, verbose_name='Additional Days')
    pickup_date = models.DateField(null=True, blank=True)
    number_of_days = models.IntegerField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True, verbose_name='Total Cost')
    additional_cost = models.IntegerField(null=True, blank=True)
    overall_cost = models.IntegerField(null=True, blank=True, verbose_name='Total Cost')
    full_range_end_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(null=True, blank=False, max_length=25)
    street = models.CharField(null=True, blank=False, max_length=255)
    city = models.CharField(null=True, blank=False, max_length=255)
    state = models.CharField(null=True, blank=False, max_length=255)
    postal_code = models.IntegerField(null=True, blank=False)
    dogs_name = models.CharField(max_length=100, null=True, blank=False)
    dogs_breed = models.CharField(max_length=100, null=True, blank=False)
    dogs_sex = models.CharField(max_length=25, null=True, blank=False, choices=(('male', 'Male'), ('female', 'Female')))
    dogs_age = models.IntegerField(null=True, blank=False)
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=(('closed','Closed'), ('active','Active'), ('upcoming','Upcoming')), null=True, blank=True)
    # repeating = models.BooleanField(default=False)
    # transfer_kennel = models.CharField(max_length=25, choices=((str(num), str(num)) for num in range(1,57)), null=True, blank=True)
    session_key = models.CharField(null=True, blank=False, max_length=255)
    shot_records = models.FileField(null=True, blank=True, upload_to='media/')

    def get_reservation_types():
        return RESERVATION_TYPES

    def get_pricing(reservation_type):
        pricing = {
            'boarding': {'price':25, 'minimum': None, 'additional_days_price': None},
            'boarding_and_training': {'price': 30, 'minimum': None, 'additional_days_price': None},
            'obedience_training': {'price': 30, 'minimum': 30, 'additional_days_price': 25},
            'retriever_training': {'price': 30, 'minimum': 60, 'additional_days_price': 25},
        }
        return pricing[reservation_type]

    def get_date_range(obj):
        start_date = obj.start_date
        end_date = obj.end_date
        if obj.pickup_date:
            end_date = obj.pickup_date
        return start_date, end_date

    @classmethod
    def get_non_overlapped(cls, reserved_dates):
        date_ranges = list()
        for obj in reserved_dates:
            start_date, end_date = cls.get_date_range(obj)
            date_range = pd.date_range(start=start_date, end=end_date).to_list()
            date_ranges.append(date_range)
        flatted_date_ranges = list([item for sublist in date_ranges for item in sublist])
        my_dict = {i:flatted_date_ranges.count(i) for i in flatted_date_ranges}
        return my_dict

    def convert_to_ranges(dates):
        start_dates = list()
        end_dates = list()
        date_ranges = list()

        if dates:
            start_dates.append(sorted(dates)[0])
            for i,e in enumerate(sorted(dates)):
                if i < len(dates)-1:
                    day_diff = abs(dates[i].date() - dates[i+1].date()).days
                    if day_diff > 1:
                        start_dates.append(dates[i+1])
                        end_dates.append(dates[i]+datetime.timedelta(days=1))
            end_dates.append(sorted(dates)[-1]+datetime.timedelta(days=1))
            
            for i in range(len(start_dates)):
                date_ranges.append({'start_date':start_dates[i].date(), 'end_date':end_dates[i].date()})
                
        return date_ranges

    @classmethod
    def get_active(cls, reservation_type=None):
        if reservation_type:
            num_active = cls.objects.filter(Q(end_date__gte=datetime.datetime.today()) | Q(pickup_date__gte=datetime.datetime.today()), type=reservation_type).count()
        else:
            num_active = cls.objects.filter(Q(end_date__gte=datetime.datetime.today()) | Q(pickup_date__gte=datetime.datetime.today()), type=reservation_type).count()
        return num_active

    @classmethod
    def get_max_reservations(cls, reservation_type):
        if reservation_type == 'boarding' or reservation_type == 'boarding_and_training':
            max_reservations = 56
        elif reservation_type == 'obedience_training' or reservation_type == 'retriever_training':
            max_reservations = 30
        return max_reservations

    @classmethod
    def get_unavailable(cls, reservation_type):
        reserved_dates = cls.objects.filter(Q(end_date__gte=datetime.datetime.today()) | Q(pickup_date__gte=datetime.datetime.today()), type=reservation_type)
        non_overlapped = cls.get_non_overlapped(reserved_dates)
        maxed_out = [k for k, v in non_overlapped.items() if v >= cls.get_max_reservations(reservation_type)]
        ranges = cls.convert_to_ranges(maxed_out)
        return ranges

    def get_end_date(self):
        end_date_additional = self.end_date_additional
        end_date = self.end_date_additional or self.end_date

        if type(self.end_date) == tuple:
            end_date = self.end_date[0]
        
        if end_date_additional:
            end_date = self.end_date_additional
            if type(self.end_date_additional) == tuple:
                end_date = self.end_date_additional[0]

        if self.pickup_date:
            end_date = self.pickup_date
            if type(self.pickup_date) == tuple:
                end_date = self.pickup_date[0]

        return end_date

    def clean(self):
        super().clean()
        kennel = self.kennel
        if kennel.booked and not self.id and not self.status == 'closed':
            raise ValidationError('This Kennel is already booked.')

    def get_expired():
        today = datetime.datetime.today()
        reservations = Reservation.objects.filter(Q(end_date__lte=today) | Q(end_date_additional__lte=today) | Q(pickup_date__lte=today))
        expire_today = [res for res in reservations if res.kennel.booked == True]
        return expire_today

    def save(self, *args, **kwargs):
        if self.end_date:
            end_date = self.get_end_date()
        if self.start_date:
            start_date = self.start_date
            if type(start_date) == tuple:
                start_date = str(start_date[0])
        if self.end_date and self.start_date:
            end_date = datetime.datetime.strptime(str(self.get_end_date()), '%Y-%m-%d').date()
            if type(start_date) == tuple:
                start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            else:
                start_date = datetime.datetime.strptime(str(start_date), '%Y-%m-%d').date()

            self.full_range_end_date = end_date

            if type(self.status) == tuple:
                if self.status[0]:
                    self.status = self.status[0]
            if not self.status == 'closed':
                if end_date > datetime.datetime.today().date() and start_date <= datetime.datetime.today().date():
                    self.status = 'active'
                if start_date > datetime.datetime.today().date():
                    self.status = 'upcoming'
                if end_date < datetime.datetime.today().date():
                    self.status = 'closed'
            if self.status == 'active':
                self.kennel.booked = True
                self.kennel.save()

            self.start_date = str(start_date)
            self.end_date = str(end_date)
            if self.start_date_additional and type(self.start_date_additional) == tuple:
                if not self.start_date_additional[0]:
                    self.start_date_additional = None
                else:
                    self.start_date_additional = str(self.start_date_additional[0])
            if self.end_date_additional and type(self.end_date_additional) == tuple:
                if not self.end_date_additional[0]:
                    self.end_date_additional = None
                else:
                    self.end_date_additional = str(self.end_date_additional[0])
            if self.pickup_date and type(self.pickup_date) == tuple:
                if not self.pickup_date[0]:
                    self.pickup_date = None
                else:
                    self.pickup_date = str(self.pickup_date[0])

            if type(self.kennel) == tuple: 
                if self.kennel[0]:
                    self.kennel = self.kennel[0]
                else:
                    self.kennel = None
            if type(self.type) == tuple: 
                if self.type[0]:
                    self.type = self.type[0]
                else:
                    self.type = None
            if type(self.extended_stay) == tuple: 
                if self.extended_stay[0]:
                    self.extended_stay = self.extended_stay[0]
                else:
                    self.extended_stay = False
            if type(self.number_of_days) == tuple: 
                if self.number_of_days[0]:
                    self.number_of_days = self.number_of_days[0]
                else:
                    self.number_of_days = None
            if type(self.cost) == tuple: 
                if self.cost[0]:
                    self.cost = self.cost[0]
                else:
                    self.cost = None
            if type(self.additional_cost) == tuple: 
                if self.additional_cost[0]:
                    self.additional_cost = self.additional_cost[0]
                else:
                    self.additional_cost = None
            if type(self.overall_cost) == tuple: 
                if self.overall_cost[0]:
                    self.overall_cost = self.overall_cost[0]
                else:
                    self.overall_cost = None
            if type(self.first_name) == tuple:
                if self.first_name[0]:
                    self.first_name = str(self.first_name[0])
                else:
                    self.first_name = None
            if type(self.last_name) == tuple: 
                if self.last_name[0]:
                    self.last_name = str(self.last_name[0])
                else:
                    self.last_name = None
            if type(self.email) == tuple: 
                if self.email[0]:
                    self.email = str(self.email[0])
                else:
                    self.email = None
            if type(self.phone) == tuple: 
                if self.phone[0]:
                    self.phone = str(self.phone[0])
                else:
                    self.phone = None
            if type(self.state) == tuple: 
                if self.state[0]:
                    self.state = str(self.state[0])
                else:
                    self.state = None
            if type(self.city) == tuple: 
                if self.city[0]:
                    self.city = str(self.city[0])
                else:
                    self.city = None
            if type(self.street) == tuple: 
                if self.street[0]:
                    self.street = str(self.street[0])
                else:
                    self.street = None
            if type(self.postal_code) == tuple: 
                if self.postal_code[0]:
                    self.postal_code = str(self.postal_code[0])
                else:
                    self.postal_code = None
            if type(self.dogs_name) == tuple: 
                if self.dogs_name[0]:
                    self.dogs_name = str(self.dogs_name[0])
                else:
                    self.dogs_name = None
            if type(self.dogs_breed) == tuple: 
                if self.dogs_breed[0]:
                    self.dogs_breed = str(self.dogs_breed[0])
                else:
                    self.dogs_breed = None
            if type(self.dogs_sex) == tuple: 
                if self.dogs_sex[0]:
                    self.dogs_sex = str(self.dogs_sex[0])
                else:
                    self.dogs_sex = None
            if type(self.dogs_age) == tuple: 
                if self.dogs_age[0]:
                    self.dogs_age = self.dogs_age[0]
                else:
                    self.dogs_age = None
            if type(self.shot_records) == tuple: 
                if self.shot_records[0]:
                    self.shot_records = self.shot_records[0]
                else:
                    self.shot_records = None
            if type(self.comments) == tuple: 
                if self.comments[0]:
                    self.comments = str(self.comments[0])
                else:
                    self.comments = None


        super(Reservation, self).save(*args, **kwargs)


# for i in range(30):
#     Reservation.objects.create(kennel=Kennel.objects.last(), start_date='2021-11-30', end_date='2021-12-03', type='obedience_training')
